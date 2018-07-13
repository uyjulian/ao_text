from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4040.bin",                # FileName
        "m4040",                    # MapName
        "m4040",                    # Location
        0x007C,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 124, 0, 1, 0, 2],
    )

    BuildStringList((
        "m4040",                  # 0
        "Ernest",                 # 1
        "Former Chairman Hartmann",# 2
        "イベント用モンスター",   # 3
        "イベント用モンスター",   # 4
        "bm4020",                 # 5
    ))

    ATBonus("ATBonus_134", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_1F4", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_214", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71800.dat", "ms71800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1F4", "MonsterBattlePostion_1D4", "ed7451", "ed7000", "ATBonus_134"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)

    ChipFrameInfo(664, 0)                                        # 0

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2DA",          # 02, 2
        "Function_3_2F7",          # 03, 3
        "Function_4_1BD6",         # 04, 4
        "Function_5_1C84",         # 05, 5
        "Function_6_1CC7",         # 06, 6
        "Function_7_1D1C",         # 07, 7
        "Function_8_1D71",         # 08, 8
        "Function_9_1DC6",         # 09, 9
        "Function_10_1E1B",        # 0A, 10
        "Function_11_1E94",        # 0B, 11
        "Function_12_1EF9",        # 0C, 12
        "Function_13_3045",        # 0D, 13
        "Function_14_3094",        # 0E, 14
        "Function_15_30C5",        # 0F, 15
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_298")

    label("loc_2B3")

    Return()

    # Function_0_298 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2D9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 12)

    label("loc_2D9")

    Return()

    # Function_1_2B4 end

    def Function_2_2DA(): pass

    label("Function_2_2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 6)), scpexpr(EXPR_END)), "loc_2EC")
    OP_70(0x0, 0x3C)
    Jump("loc_2F0")

    label("loc_2EC")

    OP_70(0x0, 0x0)

    label("loc_2F0")

    Sound(129, 1, 100, 0)
    Return()

    # Function_2_2DA end

    def Function_3_2F7(): pass

    label("Function_3_2F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("chr/ch02300.itc", 0x26)
    LoadChrToIndex("chr/ch06500.itc", 0x27)
    LoadChrToIndex("monster/ch71850.itc", 0x28)
    LoadChrToIndex("chr/ch02350.itc", 0x29)
    LoadChrToIndex("chr/ch02356.itc", 0x2A)
    LoadChrToIndex("apl/ch50014.itc", 0x2B)
    LoadChrToIndex("monster/ch71852.itc", 0x2C)
    LoadEffect(0x0, "event\\ev618_01.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\ms00002.eff")
    SoundLoad(832)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02600.itp")
    OP_68(900, 1400, -40800, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 1400, 0, -45800, 0)
    SetChrPos(0x109, 600, 0, -46900, 0)
    SetChrPos(0x10A, 2300, 0, -47800, 0)
    SetChrPos(0x108, 1500, 0, -48900, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 190, -2400, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 190, -1400, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2700, -800, 2000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -2700, -800, 2000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10000000)
    SetCameraDistance(17500, 3000)

    def lambda_56A():
        OP_97(0x101, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_56A)
    Sleep(50)

    def lambda_587():
        OP_97(0x109, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_587)
    Sleep(50)

    def lambda_5A4():
        OP_97(0x10A, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5A4)
    Sleep(50)

    def lambda_5C1():
        OP_97(0x108, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5C1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x10A, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x108, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007F(There they are...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00601F#6P(We managed to catch up...?)\x02",
    )

    CloseMessageWindow()
    OP_68(0, 500, 1800, 4500)
    MoveCamera(315, 30, 0, 4500)
    OP_6E(650, 4500)
    SetCameraDistance(45000, 4500)
    BeginChrThread(0x9, 3, 0, 4)
    BeginChrThread(0x8, 3, 0, 5)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1200, 4500, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(16500, 2000)
    OP_0D()
    WaitChrThread(0x9, 3)
    TurnDirection(0x9, 0x8, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#30WE-Ernest...\x01",
            "Just let me go already...!\x02\x03",
            "I-I don't want to do this anymore!\x02",
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
    WaitChrThread(0x8, 3)

    ChrTalk(
        0x8,
        (
            "#6P#02604FOh geez, Chairman, that would be a problem.\x02\x03",
            "#02610FI need you to make a comeback in\x01",
            "the political world of Crossbell...\x02\x03",
            "To make me the next mayor too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02701F#11PJ-Just cut it out already!\x02\x03",
            "A comeback in the political world!?\x01",
            "Do you really think that's even\x01",
            "remotely possible at this point?\x02\x03",
            "Besides, you aren't thinking that\x01",
            "someone like you could take away\x01",
            "Dieter Crois's position as mayor!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#02613FHeheh, but that's easy.\x02\x03",
            "Maybe not as human. But once I reach out\x01",
            "to the true "God", it'll be child's play...\x02\x03",
            "#02610FWith the wisdom to see karma in its entirety,\x01",
            "I could manipulate reality as I see fit...\x02\x03",
            "#02614FYes... Just like the great\x01",
            "master, Joachim Gｸnther.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#02705F#11PY-You're a madman...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2091, 255, 100, 0)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#30WWe won't let you...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B3B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B3B)
    Fade(500)
    OP_68(700, 900, -18500, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25500, 0)
    OP_68(0, 1200, 500, 6000)
    MoveCamera(323, 15, 0, 6000)
    SetCameraDistance(17500, 6000)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 7)
    Sleep(500)
    BeginChrThread(0x10A, 3, 0, 8)
    Sleep(500)
    BeginChrThread(0x108, 3, 0, 9)
    OP_6F(0x79)
    OP_96(0x9, 0x2BC, 0xBE, 0x11F8, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        "#02700FW-Who are you people!?\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Hu hu. So you finally\x01",
            "managed to catch up?\x02\x03",
            "Or should I say "long time no see"?\x01",
            "Lloyd, and Dudley.\x02\x03",
            "Thank you for your hard\x01",
            "work in Altair City.\x02",
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
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        "#00013F#6PErnest... You...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x108, 3)

    ChrTalk(
        0x10A,
        (
            "#6P#00601FAre you implying you knew we\x01",
            "would be coming after you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02613F#11PHeheh, all thanks to the\x01",
            "power of the great "Gnosis".\x02\x03",
            "You following our whereabouts,\x01",
            "your arrival in Altair City...\x02\x03",
            "Locating us, and getting approval\x01",
            "of the Republican army to track us\x01",
            "down up to this point...\x02\x03",
            "#02610FI foresaw it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#6PKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10113FHow could you possibly know all this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01408F#6PLooks like he was able to sense our moves\x01",
            "through some mysterious perceptual ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02705FW-Wait, that means you're\x01",
            "from the Crossbell Police?\x02\x03",
            "#02703F...Dammit, I see no other wait out!\x02\x03",
            "#02701FPlease, I'll turn myself in!\x01",
            "Just arrest this lunatic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02613F#11POh my. "Lunatic"? That's rude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PThat goes without saying...\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, -200, 190, -1300, 1500, 0x0)
    SetChrChipByIndex(0x101, 0x2B)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#6P──Former Chairman Hartmann\x01",
            "and Ernest Reis!\x02\x03",
            "In accordance with autonomous state law, you're\x01",
            "hereby under arrest and charged for breaking out\x01",
            "of prison and numerous other crimes. \x02\x03",
            "Quietly surrender at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02610F#11PHeheh. Why the rush?\x02\x03",
            "#02613FToday, I will succeed master Joachim\x01",
            "and open to the door to "D"...\x02\x03",
            "#02614FIt's not too late for a bit\x01",
            "of entertainment, right!?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x108,
        "#01401F#6PMh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 1200, 3300, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(16500, 3000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 70, 0)
    Sound(531, 0, 50, 0)
    Sleep(500)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, 0, 200, 3300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(832, 2, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    Sound(817, 0, 100, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 2700, 200, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, -2700, 200, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_1342():
        OP_96(0xFE, 0xA8C, 0xC8, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1342)

    def lambda_135C():
        OP_96(0xFE, 0xFFFFF574, 0xC8, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_135C)

    def lambda_1376():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1376)

    def lambda_1387():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1387)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_1427():
        OP_96(0xFE, 0xFFFFFF38, 0xBE, 0xFFFFF380, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1427)
    Sleep(300)

    def lambda_1444():
        OP_96(0xFE, 0xC8, 0xBE, 0xFFFFEC78, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1444)
    Sleep(100)

    def lambda_1461():
        OP_96(0xFE, 0x5DC, 0xBE, 0xFFFFEDA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1461)
    Sleep(100)

    def lambda_147E():
        OP_96(0xFE, 0xFFFFFA24, 0xBE, 0xFFFFEF34, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_147E)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    WaitChrThread(0x108, 1)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(932, 0, 100, 0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    OP_68(0, 1200, -300, 2500)
    MoveCamera(327, 15, 0, 2500)
    SetCameraDistance(17000, 2500)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    Fade(250)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_24(0x340)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(
        0x9,
        "#02705FE-Eeeeeeeek!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#3P#10110F#6PT-These are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#6P#00607F#6PSome kind of archaisms!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1624")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆Zero NG+ Quest Clear\x01",      # 0
            "◆Not Cleared\x01",               # 1
            "◆No Change\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_160B"),
        (1, "loc_1615"),
        (2, "loc_161F"),
        (SWITCH_DEFAULT, "loc_161F"),
    )


    label("loc_160B")

    OP_29(0x34, 0x4, 0x10)
    Jump("loc_1624")

    label("loc_1615")

    OP_29(0x34, 0x3, 0x10)
    Jump("loc_1624")

    label("loc_161F")

    Jump("loc_1624")

    label("loc_1624")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1755")

    ChrTalk(
        0x101,
        (
            "#00010F#6PThese are the magic dolls that froze\x01",
            "over Geofront B2-Division...!\x02\x03",
            "#00007FWatch out! These are\x01",
            "dangerous opponents!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02613F#11PHeheh. Lady and gentlemen,\x01",
            "please excuse us for now.\x02\x03",
            "#02614FIn the meanwhile, have fun with these\x01",
            "guardians left behind by Master Joachim.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187A")

    label("loc_1755")


    ChrTalk(
        0x101,
        (
            "#00005F#6PThe Middle Ages magic dolls\x01",
            "that Joachim controlled...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02613F#11PHeheh, oh no. These are\x01",
            "far stronger than those.\x02\x03",
            "#02610F──Well then, lady and gentlemen,\x01",
            "please excuse us for now.\x02\x03",
            "#02614FIn the meanwhile, have fun with these\x01",
            "guardians left behind by Master Joachim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187A")

    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    OP_68(1000, 1200, 3700, 4000)

    def lambda_189F():
        OP_96(0xFE, 0x12C, 0xC8, 0x13EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_189F)
    WaitChrThread(0x8, 1)
    OP_64(0x9)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 10)
    BeginChrThread(0x9, 3, 0, 11)
    Sleep(3500)

    ChrTalk(
        0x109,
        "#10107FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00610FTsk, you won't get away...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1200, -300, 0)
    MoveCamera(327, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0xA, 3000, 200, 2500, 180)
    SetChrPos(0xB, -1000, 200, 2500, 180)
    OP_0D()
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)

    def lambda_1977():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1977)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2, 0x1, 0xFF, 0x0, 3000, 2000, 2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(881, 0, 50, 0)
    EndChrThread(0xB, 0x0)
    SetChrChipByIndex(0xB, 0x2C)
    SetChrSubChip(0xB, 0x0)

    def lambda_19FA():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_19FA)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2, 0x2, 0xFF, 0x0, -1000, 2000, 2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x108,
        (
            "#01403F#6PIt looks like these monsters are \x01",
            "unlike your average opponent...\x02\x03",
            "#01407FDon't hold back now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#6PYes!\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 500)
    OP_68(0, 1200, 1000, 500)

    def lambda_1B13():
        OP_97(0x101, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B13)
    Sleep(30)

    def lambda_1B30():
        OP_97(0x108, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1B30)
    Sleep(30)

    def lambda_1B4D():
        OP_97(0x10A, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1B4D)
    Sleep(30)

    def lambda_1B6A():
        OP_97(0x109, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B6A)
    Sleep(500)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x108, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x109, 0xFF)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Battle("BattleInfo_214", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 12)
    Return()

    # Function_3_2F7 end

    def Function_4_1BD6(): pass

    label("Function_4_1BD6")

    Sleep(1000)

    def lambda_1BDE():
        OP_95(0xFE, 0, 190, 600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BDE)
    WaitChrThread(0x9, 1)
    Sleep(500)

    def lambda_1BFF():
        OP_95(0xFE, 0, 190, 2600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BFF)
    WaitChrThread(0x9, 1)
    Sleep(500)

    def lambda_1C20():
        OP_95(0xFE, 0, 190, 4600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C20)
    WaitChrThread(0x9, 1)
    OP_A6(0x9, 0x0, 0x32, 0x12C, 0x7D0)
    Sleep(200)

    def lambda_1C54():
        OP_95(0xFE, 0, 190, 5600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C54)
    WaitChrThread(0x9, 1)
    OP_A6(0x9, 0x0, 0x32, 0x12C, 0x7D0)
    Sleep(200)
    Return()

    # Function_4_1BD6 end

    def Function_5_1C84(): pass

    label("Function_5_1C84")

    Sleep(3000)

    def lambda_1C8C():
        OP_95(0xFE, 0, 190, 700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C8C)
    WaitChrThread(0x8, 1)
    Sleep(1500)

    def lambda_1CAD():
        OP_95(0xFE, 0, 190, 3300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CAD)
    WaitChrThread(0x8, 1)
    Return()

    # Function_5_1C84 end

    def Function_6_1CC7(): pass

    label("Function_6_1CC7")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFFFF38, 0xBE, 0xFFFFF63C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_6_1CC7 end

    def Function_7_1D1C(): pass

    label("Function_7_1D1C")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xC8, 0xBE, 0xFFFFF060, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_7_1D1C end

    def Function_8_1D71(): pass

    label("Function_8_1D71")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0x5DC, 0xBE, 0xFFFFF18C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_8_1D71 end

    def Function_9_1DC6(): pass

    label("Function_9_1DC6")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFFFA24, 0xBE, 0xFFFFF31C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_1DC6 end

    def Function_10_1E1B(): pass

    label("Function_10_1E1B")


    def lambda_1E20():
        OP_96(0xFE, 0x1004, 0x0, 0x39D0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E20)

    def lambda_1E3A():
        OP_96(0xFE, 0x1194, 0x0, 0x37DC, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E3A)
    WaitChrThread(0x8, 1)

    def lambda_1E58():
        OP_96(0xFE, 0x19C8, 0x60E, 0x6C98, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E58)
    WaitChrThread(0x9, 1)

    def lambda_1E76():
        OP_96(0xFE, 0x1B58, 0x60E, 0x6AA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E76)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Return()

    # Function_10_1E1B end

    def Function_11_1E94(): pass

    label("Function_11_1E94")


    ChrTalk(
        0x9,
        "#12P#11A#02700FL-Let me go...\x02",
    )

    Sleep(1100)
    OP_57(0x0)
    OP_5A()
    Sleep(400)
    OP_82(0xC8, 0x0, 0xBB8, 0x4B0)

    ChrTalk(
        0x9,
        "#6P#12A#4SLet me goooooooooo!\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_11_1E94 end

    def Function_12_1EF9(): pass

    label("Function_12_1EF9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("chr/ch00053.itc", 0x26)
    LoadChrToIndex("chr/ch02953.itc", 0x27)
    LoadChrToIndex("monster/ch71850.itc", 0x28)
    LoadChrToIndex("chr/ch00953.itc", 0x29)
    LoadChrToIndex("apl/ch51021.itc", 0x2A)
    SoundLoad(4039)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    OP_68(2000, 1300, 2000, 0)
    MoveCamera(320, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 1400, 190, -500, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x109, 400, 190, -1400, 0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x3)
    SetChrPos(0x10A, 3500, 190, -700, 0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x3)
    SetChrPos(0x108, -500, 190, 700, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 3000, 200, 5000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2071():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2071)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, 0, 200, 5000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0xB, 0x0)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_20E2():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_20E2)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(18000, 3000)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_217C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_217C)

    def lambda_218D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_218D)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)

    def lambda_221D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_221D)
    WaitChrThread(0x101, 2)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    ChrTalk(
        0x101,
        "#6P#00015F#30W...Argh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#3P#10106F#30WW-What strength...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00610FTsk...\x01",
            "What a waste of time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#01407FOkay, let's chase after them!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(531, 0, 80, 0)
    Sound(540, 0, 60, 0)
    BeginChrThread(0x108, 3, 0, 14)
    Sleep(300)
    BeginChrThread(0x10A, 3, 0, 13)
    Sleep(1000)
    Fade(500)
    OP_68(4900, 900, 13000, 0)
    MoveCamera(300, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(7000, 4100, 33300, 6500)
    MoveCamera(327, 15, 0, 6500)
    SetCameraDistance(16500, 6500)
    WaitChrThread(0x10A, 3)
    OP_6F(0x79)

    ChrTalk(
        0x10A,
        (
            "#00607F#11PWhat's the matter this time?\x01",
            "Can't you move?!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 3)
    OP_93(0x108, 0xB4, 0x1F4)
    Fade(500)
    OP_68(2700, 1200, -500, 0)
    MoveCamera(320, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 2700, 190, -500, 0)
    SetChrPos(0x109, 1500, 190, -1400, 0)
    OP_0D()

    def lambda_240F():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_240F)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    SetChrSubChip(0x101, 0x1)
    Sound(2030, 255, 60, 0)
    Sleep(200)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00007FI'm... I'm fine...!\x02",
    )

    CloseMessageWindow()

    def lambda_2476():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2476)
    SetChrSubChip(0x109, 0x2)
    Sleep(120)
    SetChrSubChip(0x109, 0x1)
    Sound(2463, 255, 60, 0)
    Sleep(120)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10101FSo do I... Somehow...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(7000, 4100, 33300, 0)
    MoveCamera(327, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x108,
        "#01407FDudley! Above you!\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(809, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x5DC)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChip(0x0, 0x10A, 0x1E, 0x12C)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)

    def lambda_25AC():
        OP_9D(0xFE, 0x1C20, 0x1194, 0xA21C, 0x708, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_25AC)
    Sound(3447, 255, 100, 0)
    Sound(834, 0, 100, 0)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x29)
    SetChrSubChip(0x10A, 0x3)
    SetChrChip(0x1, 0x10A, 0x0, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x7D0)
    OP_71(0x0, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    Sound(166, 0, 90, 0)
    Sound(189, 0, 90, 0)
    OP_79(0x0)
    Sound(189, 0, 90, 0)
    Sound(833, 0, 90, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    Sleep(1000)
    Sound(2563, 255, 100, 0)

    ChrTalk(
        0x10A,
        "#00610FWhat...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5000, 1100, 23200, 0)
    MoveCamera(317, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 4700, 0, 15000, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 3000, 0, 15300, 0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_68(9800, 3700, 24500, 2000)
    MoveCamera(327, 13, 0, 2000)
    SetCameraDistance(19000, 2000)

    def lambda_26E1():
        OP_96(0xFE, 0x16A8, 0x64, 0x59D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26E1)
    Sleep(200)

    def lambda_26FE():
        OP_96(0xFE, 0x1004, 0x64, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_26FE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FT-The path...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10110FN-No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    OP_0D()

    def lambda_2767():
        OP_96(0xFE, 0x1F40, 0x1194, 0xA604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2767)
    WaitChrThread(0x108, 1)

    ChrTalk(
        0x108,
        (
            "#01403FTrembles from the battle caused\x01",
            "the weaker gravel to collapse...\x02\x03",
            "#01400FThe gap is too far \x01",
            "to just leap across.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PYes...I think so too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#5PI-I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606FTsk...\x01",
            "Nothing to do about it now.\x02\x03",
            "#00607FJust wait there!\x01",
            "We'll settle things alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FN-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FEven you two shouldn't rush\x01",
            "in without proper support...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01400FNo──\x01",
            "Let's act separately.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2969():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_2969)

    ChrTalk(
        0x101,
        "#00005FWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#6P#00605FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#01403FThere are two routes\x01",
            "leading to the depths.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x108, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x108,
        "#01400F#6PThis way is one of them.\x02",
    )

    CloseMessageWindow()
    OP_68(26000, -9000, 29000, 4000)
    MoveCamera(340, 15, 0, 4000)
    OP_6E(650, 4000)
    SetCameraDistance(45500, 4000)

    def lambda_2A43():
        OP_93(0x10A, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2A43)
    Sleep(100)

    def lambda_2A53():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A53)
    Sleep(100)

    def lambda_2A63():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A63)
    Sleep(100)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#N#5PAnd the other one...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10100F#N#5PCould that be the other one...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x108,
        (
            "#01404F#12P#N#5PExactly. It's the longer one of the two,\x01",
            "but we should end up in the same room.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(7600, 5400, 42100, 0)
    MoveCamera(317, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0x10A,
        "#00603F#5PThen that settles it!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#00607F#11PBannings! Master Segeant Seeker!\x01",
            "We'll go ahead and pursue them!\x02\x03",
            "Meet with us later in some way!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C1B():
        OP_93(0x101, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C1B)
    Sleep(0)

    def lambda_2C2B():
        OP_93(0x109, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C2B)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    def lambda_2C43():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2C43)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00007FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FYes sir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x108,
        (
            "#01404F#4039V#11P#30WGood luck──\x01",
            "And be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFC7)
    OP_C9(0x1, 0x80000000)
    OP_68(7600, 5400, 46100, 2500)
    SetCameraDistance(19500, 2500)
    BeginChrThread(0x108, 3, 0, 15)
    Sleep(300)
    BeginChrThread(0x10A, 3, 0, 15)
    WaitChrThread(0x108, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(5000, 1000, 23200, 0)
    MoveCamera(317, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    EndChrThread(0x108, 0x3)
    EndChrThread(0x10A, 0x3)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00003FOkay... We should hurry too!\x02\x03",
            "#00001FMaster Sergeant, can you move?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10101F#5PYeah, I'm fine.\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10105F#5PBy the way, Mr. Lloyd...\x02\x03",
            "#10100FHow about we give those Crafts\x01",
            "that can be combined a go?\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002F#12PSounds like a good idea.\x02\x03",
            "#00004FWe know each other's traits, so that\x01",
            "shouldn't be much of a problem.\x02\x03",
            "#00000FLet's give it a try and\x01",
            "move on carefully!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2442, 255, 100, 0)

    ChrTalk(
        0x109,
        "#10109F#5P#30WYes!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F42")
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)
    Jump("loc_2F4A")

    label("loc_2F42")

    AddCraft(0x0, 0x18C)
    AddCraft(0x8, 0x18C)

    label("loc_2F4A")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Noｱl learned the\x01\x07\x02",
            ""Brave Hearts"\x07\x05",
            " Combi Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x9, 0x0)
    RemoveParty(0x7, 0x0)
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
    OP_D7(0x2A)
    OP_37()
    SetChrPos(0x0, 5270, 100, 23060, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 6)
    OP_29(0xA0, 0x1, 0x2)
    ClearScenarioFlags(0x21, 0)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_1EF9 end

    def Function_13_3045(): pass

    label("Function_13_3045")

    OP_96(0xFE, 0x1324, 0x0, 0x3A98, 0x1388, 0x1)

    def lambda_305E():
        OP_95(0xFE, 7000, 3200, 33300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_305E)
    Sleep(3000)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_3045 end

    def Function_14_3094(): pass

    label("Function_14_3094")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0x1324, 0x0, 0x3A98, 0x157C, 0x1)
    OP_95(0xFE, 7200, 4500, 43800, 5500, 0x0)
    Return()

    # Function_14_3094 end

    def Function_15_30C5(): pass

    label("Function_15_30C5")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_96(0xFE, 0x1D4C, 0x1194, 0xE678, 0x1388, 0x0)
    Return()

    # Function_15_30C5 end

    SaveToFile()

Try(main)
