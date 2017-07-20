from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4290.bin",                # FileName
        "m4290",                    # MapName
        "m4290",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4290",                  # 0
        "Dr. Novartis",       # 1
        "Clown Campanella",     # 2
        "Ariane Road",         # 3
        "Silver",                     # 4
        "Lisha",               # 5
        "Mushroute Scott",         # 6
        "Wrestler Wenzel",     # 7
        "Arios",               # 8
        "Daughter of a knight-costume",           # 9
        "Daughter of a knight-costume",           # 10
        "Daughter of a knight-costume",           # 11
        "Spinkimeira",       # 12
        "SE control",                 # 13
        "For APL display",              # 14
        "bm4210",                 # 15
    ))

    ATBonus("ATBonus_24C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_30C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_32C", 0x0042, 72, 6, 45, 3, 3, 30, 0, "bm4210", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_2EC", "ed7454", "ed7453", "ATBonus_24C"),
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1052, 0)                                       # 0

    ScpFunction((
        "Function_0_41C",          # 00, 0
        "Function_1_43D",          # 01, 1
        "Function_2_480",          # 02, 2
        "Function_3_254B",         # 03, 3
        "Function_4_2587",         # 04, 4
        "Function_5_25C3",         # 05, 5
        "Function_6_25FF",         # 06, 6
        "Function_7_263B",         # 07, 7
        "Function_8_2677",         # 08, 8
        "Function_9_26A9",         # 09, 9
        "Function_10_29B0",        # 0A, 10
        "Function_11_2A37",        # 0B, 11
        "Function_12_2B00",        # 0C, 12
        "Function_13_2B09",        # 0D, 13
        "Function_14_2B12",        # 0E, 14
        "Function_15_2B1B",        # 0F, 15
        "Function_16_2B24",        # 10, 16
        "Function_17_2B2D",        # 11, 17
        "Function_18_2B36",        # 12, 18
        "Function_19_6A7E",        # 13, 19
        "Function_20_6AA0",        # 14, 20
        "Function_21_6BEC",        # 15, 21
        "Function_22_6BFF",        # 16, 22
        "Function_23_6CF4",        # 17, 23
        "Function_24_6D5E",        # 18, 24
        "Function_25_6D7D",        # 19, 25
        "Function_26_6E8E",        # 1A, 26
        "Function_27_6EFA",        # 1B, 27
        "Function_28_6FA6",        # 1C, 28
        "Function_29_7046",        # 1D, 29
        "Function_30_70E6",        # 1E, 30
        "Function_31_718C",        # 1F, 31
        "Function_32_722C",        # 20, 32
        "Function_33_72C5",        # 21, 33
        "Function_34_73FD",        # 22, 34
        "Function_35_7520",        # 23, 35
        "Function_36_7533",        # 24, 36
        "Function_37_7568",        # 25, 37
        "Function_38_765A",        # 26, 38
        "Function_39_7675",        # 27, 39
        "Function_40_76B5",        # 28, 40
        "Function_41_76F3",        # 29, 41
        "Function_42_770C",        # 2A, 42
    ))


    def Function_0_41C(): pass

    label("Function_0_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42D")
    Event(0, 2)

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_43C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)

    label("loc_43C")

    Return()

    # Function_0_41C end

    def Function_1_43D(): pass

    label("Function_1_43D")

    SoundDistance(0x7A, 0xFFFFB06E, 0xBC2, 0xFFFFD008, 0x4E20, 0x186A0, 0x64, 0x0)
    OP_E3(0x24E, 0xFFFFFD12, 0x6004)
    OP_E3(0x7DBD, 0xFFFFFD12, 0x14DC)
    Sound(123, 1, 80, 0)
    SetMapObjFlags(0x0, 0x4)
    Return()

    # Function_1_43D end

    def Function_2_480(): pass

    label("Function_2_480")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    SoundLoad(3887)
    SoundLoad(3888)
    SoundLoad(3889)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E0")
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    Jump("loc_4E6")

    label("loc_4E0")

    LoadChrToIndex("chr/ch03050.itc", 0x25)

    label("loc_4E6")

    LoadEffect(0x7, "event/ev10008.eff")
    LoadEffect(0x0, "event/ev10017.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    SetChrPos(0x101, -800, -750, -26000, 0)
    SetChrPos(0x102, 600, -750, -26000, 0)
    SetChrPos(0x103, -1100, -750, -27400, 0)
    SetChrPos(0x104, 900, -750, -27400, 0)
    SetChrPos(0x106, -800, -750, -28800, 0)
    SetChrPos(0xF4, 600, -750, -28800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 315)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 45)
    SetChrFlags(0xA, 0x8000)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0x13)
    OP_68(-290, 750, -25000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    OP_68(-720, 2250, -20050, 3000)
    MoveCamera(52, 18, 0, 3000)
    OP_6E(750, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_6DF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DF)
    Sleep(100)

    def lambda_6F7():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F7)
    Sleep(50)

    def lambda_70F():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_70F)
    Sleep(50)

    def lambda_727():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_727)
    Sleep(50)

    def lambda_73F():
        OP_9B(0x0, 0xF4, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_73F)
    Sleep(50)

    def lambda_757():
        OP_9B(0x0, 0x106, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_757)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 2)
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
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P(T-this is!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12P#N(Amazing … … enormous energy\x01",
            "It seems they are gathering ……)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00311F#12P(in addition……\x01",
            "After all it seems I lived. )\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetCameraDistance(12000, 4000)
    OP_68(-800, 2250, 1500, 4000)
    MoveCamera(0, 14, 0, 4000)
    OP_6E(810, 4000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Fade(500)
    OP_68(-800, 12550, 2650, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(5000, 0)
    OP_68(-800, 2750, 1500, 5000)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#04809F#6PUhufu …\x01",
            "This is a terrible place.\x02\x03",
            "#04800FIf it is activated so far\x01",
            "Are you ready for it soon?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "A man in white robe",
        "#04704F#11PHaha, that's right\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x86, 0x1F4)
    Sleep(200)

    NpcTalk(
        0x8,
        "A man in white robe",
        (
            "#04702F#5PYes, yeah, it's funny.\x01",
            "It seems to be a spectacle.\x02\x03",
            "\"White face\" If you live\x01",
            "I wonder if you had enjoyed it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#04809F#11PAhah, I think that's for sure\x02\x03",
            "#04805FBut, in addition to Dr.\x01",
            "I wish my professor came to crossbell\x01",
            "I wonder if I can not keep up with it?\x02\x03",
            "#04802F\"ark#4RGlorious#\"Take it out\x01",
            "Or selling quarrels to two major powers.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "A man in white robe",
        (
            "#04709F#5PHaha, that is it\x01",
            "It seems pretty interesting, is not it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "People of armor",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P….\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE7():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE7)

    def lambda_BFC():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BFC)

    def lambda_C11():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C11)

    def lambda_C26():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C26)

    def lambda_C3B():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_C3B)

    def lambda_C50():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x87, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#04805F#5PHuh? What's wrong?\x02\x03",
            "#04800FAfter all this mission,\x01",
            "Is not it easy to get rid of it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "People of armor",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P── All is his will.\x01",
            "There is no objection etc.\x02\x03",
            "Better than that, Campanella.\x01",
            "The talk is that much.\x02\x03",
            "It appears we have visitors\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-800, 2250, -4500, 2500)
    MoveCamera(0, 25, 0, 2500)
    SetCameraDistance(16000, 2500)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(50)

    def lambda_DD5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DD5)
    Sleep(50)

    def lambda_DE5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_DE5)
    WaitChrThread(0x101, 1)

    def lambda_DF6():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF6)
    Sleep(50)

    def lambda_E0E():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0E)
    Sleep(50)

    def lambda_E26():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E26)
    Sleep(50)

    def lambda_E3E():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E3E)
    Sleep(50)

    def lambda_E56():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_E56)
    Sleep(50)

    def lambda_E6E():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_E6E)
    OP_6F(0x79)
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(10290, 0)
    SetCameraDistance(9290, 2000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#12P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#12PY-you are…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12P#N… … apparently more than expected\x01",
            "It seems that all the things came together.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04805F#5POh it's you guys\x02\x03",
            "#04804FThe sneakers of the prime minister\x01",
            "You ought to be unstable … …\x02\x03",
            "#04802FUhufu, how are you\x01",
            "Did you find this place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F… ….#12P#NOnce, in terms of trade secrets.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NHowever, something interesting\x01",
            "I guess they were missing out … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E9")

    ChrTalk(
        0x109,
        (
            "#10107F#12P#NYour plan …\x01",
            "I can not overlook!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_10E9")


    ChrTalk(
        0x105,
        (
            "#10302F#12P#NAs expected to overlook\x01",
            "Have you stopped going?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112D")

    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "A man in white robe",
        (
            "#04703F#5PHmm\x02\x03",
            "#04701FTo imply Cross Bell police\x01",
            "Is it like a rookie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… ….#12PCrossbell Police,\x01",
            "It is a person of \"mission support section\".\x02\x03",
            "#00008FAssociation \"Serving meat snake#10RUroboros#\"of\x01",
            "I can see it as an official … …\x02\x03",
            "#00001FFirst of all, you can prove your identity\x01",
            "Shall I present it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "A man in white robe",
        (
            "#04705F#5PProof of status … …?\x01",
            "What is he talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04806F#5PWell, I will proceed as a police\x01",
            "Are not you stepping on?\x02\x03",
            "#04802FUhufu, we have to prove to our opponent\x01",
            "I think only as a bad joke.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "People of armor",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PThe're quite the righteous young ones\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "People of armor",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PI can not respond to requests\x01",
            "I have a hard time … ….\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F… ….#11PIt is useless, Lloyd.\x02\x03",
            "#00301FThose common sense pass through\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#NPer group of \"cults\"\x01",
            "You should think that it is the same.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x8,
        "A man in white robe",
        (
            "#04703F#5PHm, what will be done with them\x01",
            "That's not funny.\x02\x03",
            "#04702FHuh … I think it would be nice.\x01",
            "Do not try to introduce yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x8, 0x0, 0x190, 0x320, 0x0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("A man in white robe")

    AnonymousTalk(
        0xFF,
        (
            "My name is F Nobaltisse\x02\x03",
            "\"Eating snake#10RUroboros#\"In the sixth pillar of,\x01",
            "\"Thirteen studio\" is entrusted.\x02\x03",
            "Huh, please feel free\x01",
            "Please call me \"Doctor\".\x02",
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
        0x103,
        (
            "#00203F#12P#N……I see.\x01",
            "It was your job.\x02\x03",
            "#00201FIt was used for hacking the power net\x01",
            "It was that I developed inexplicable code.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04705F#1Pcheek……! Is it?\x01",
            "Do you know that code! Is it?\x02\x03",
            "#04709FThat is \"Star Hin#4RAstral#Tell me the code \"!\x01",
            "It is used in the network of association ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#04801F#5PProfessor, Professor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04703F#5PBy the way, it is a subject of the cult\x01",
            "Epstein guys picked up\x01",
            "Daughter was there ……\x02\x03",
            "#04702F─ ─ How about you! Is it?\x01",
            "For that talent for \"association\"\x01",
            "Are not you planning to make use of it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12P#NI refuse\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x8,
        "#04705F#5P#4SGaaah\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x9,
        (
            "#04806F#5PAbsolutely …\x01",
            "Just because I ran into Ren\x01",
            "Would not it be desperate as expected?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04701F#5PBesides, another story about Ren\x01",
            "It does not matter here?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "People of armor",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5PI guess I'm next\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0x0, 0x190, 0x320, 0x0)
    Fade(500)
    OP_68(-3520, 2450, 2610, 0)
    MoveCamera(53, 7, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(7100, 0)
    OP_0D()
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetChrName("People of armor")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3887V#40WMy name is Arianrod\x02\x03",
            "#3888V\"Eating snake#10RUroboros#\"In the seventh pillar of it,\x01",
            "It is crowned with the name \"steel\".\x02\x03",
            "#3889VNice to meet you\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF31)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#00011F#12P#NAh\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00108F#12P#NWhat a cool voice\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NI am wearing Gotsui armor,\x01",
            "You look like a woman ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE1")

    ChrTalk(
        0x109,
        (
            "#10108F#12P#NAnd then it's incredible\x01",
            "I feel intimidate, but ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1F")

    label("loc_1BE1")


    ChrTalk(
        0x105,
        (
            "#10301F#12P#N…… Incredible\x01",
            "It's intimidating though ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1F")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#N… …. You are \"association\"\x01",
            "Is it the strongest user?\x02\x03",
            "It certainly shuddered\x01",
            "It sounds like an owner of ___\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2330, 1950, -5470, 2000)
    MoveCamera(14, 13, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9290, 2000)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0xF4, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 5)
    BeginChrThread(0x104, 3, 0, 6)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x102, 3, 0, 4)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x106, 3)
    Sleep(150)

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#6P── This \"silver#2RIn#\"In front of you\x01",
            "I can afford that, how much can I keep?\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#11P#NHmm\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00011F#5PHey, Yin\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PWhy are you…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04804F#5P#NUhuh, quite interesting\x01",
            "I think it's a fighting card ….\x02\x03",
            "#04800FBefore that, here's Nushi\x01",
            "It seems they came back.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    def lambda_1EF0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EF0)
    Sleep(50)

    def lambda_1F00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F00)
    Sleep(50)

    def lambda_1F10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F10)
    Sleep(50)

    def lambda_1F20():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F20)
    Sleep(50)

    def lambda_1F30():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1F30)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00005F#6PWhat\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F87")

    ChrTalk(
        0x109,
        "#10105F#12PMaster…\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA6")

    label("loc_1F87")


    ChrTalk(
        0x105,
        "#10305F#12PMaster…\x02",
    )

    CloseMessageWindow()

    label("loc_1FA6")

    Sleep(100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)

    ChrTalk(
        0x103,
        (
            "#00208F#6PI feel a huge aura!\x02\x03",
            "#00207FA large Cryptid is coming!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(11290, 5000)

    def lambda_20A1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20A1)
    Sleep(50)

    def lambda_20B1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20B1)
    Sleep(50)

    def lambda_20C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20C1)
    Sleep(50)

    def lambda_20D1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20D1)
    Sleep(50)

    def lambda_20E1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_20E1)
    Sleep(50)

    def lambda_20F1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_20F1)
    Sleep(150)

    ChrTalk(
        0x104,
        "#00307F#5PWhat!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2155")

    ChrTalk(
        0x109,
        "#10101F#5PWhere, from …! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2179")

    label("loc_2155")


    ChrTalk(
        0x105,
        "#10308F#5PFrom where?!\x02",
    )

    CloseMessageWindow()

    label("loc_2179")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 35000, 7000, -1870, 270)
    OP_93(0x13, 0x10E, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x5A)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0xE5)
    OP_68(8260, 2850, -1360, 0)
    MoveCamera(72, 16, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(11450, 0)
    Fade(500)
    BeginChrThread(0x13, 0, 0, 9)
    WaitChrThread(0x13, 0)

    def lambda_2210():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2210)
    Sleep(50)

    def lambda_2220():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2220)
    Sleep(50)

    def lambda_2230():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2230)
    Sleep(50)

    def lambda_2240():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2240)
    Sleep(50)

    def lambda_2250():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2250)
    Sleep(50)

    def lambda_2260():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2260)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0xF4, 0)
    OP_6F(0x79)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0xF4, 2)
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(50)
    BeginChrThread(0xF4, 3, 0, 16)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Sleep(500)
    SetChrPos(0x101, -1040, -750, -890, 90)
    SetChrPos(0x102, -2590, -750, 20, 90)

    ChrTalk(
        0x101,
        "#00007F#6P#NAh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00110F#6P#NThis monster is\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04804F#6P#NThe Cryptid Sufin Kimail\x02\x03",
            "#04802FAn old fantasy created\x01",
            "Is it such as the keeper of the sacred flower garden?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04704F#6P#NNo, these things\x01",
            "What is realized … …\x02\x03",
            "#04702FHuh, this also to the accuracy of the plan\x01",
            "It is that you can have expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x13, 0, 0, 10)
    WaitChrThread(0x13, 0)
    OP_68(-830, 2050, -5110, 2000)
    MoveCamera(52, 7, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(14680, 2000)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00010F#6P#NUgh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#NTits …!\x01",
            "Target them if you aim for it!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#6P#N── The story is back!\x01",
            "Promptly surrender#4RAsakusa#To do!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x13, 0, 0, 11)
    WaitChrThread(0x13, 0)
    Battle("BattleInfo_32C", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 18)
    Return()

    # Function_2_480 end

    def Function_3_254B(): pass

    label("Function_3_254B")


    def lambda_2550():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2550)

    def lambda_2565():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2565)
    WaitChrThread(0xFE, 2)

    def lambda_2576():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2576)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_3_254B end

    def Function_4_2587(): pass

    label("Function_4_2587")


    def lambda_258C():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_258C)

    def lambda_25A1():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25A1)
    WaitChrThread(0xFE, 2)

    def lambda_25B2():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25B2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_2587 end

    def Function_5_25C3(): pass

    label("Function_5_25C3")


    def lambda_25C8():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25C8)

    def lambda_25DD():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25DD)
    WaitChrThread(0xFE, 2)

    def lambda_25EE():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25EE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_25C3 end

    def Function_6_25FF(): pass

    label("Function_6_25FF")


    def lambda_2604():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2604)

    def lambda_2619():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2619)
    WaitChrThread(0xFE, 2)

    def lambda_262A():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_262A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_25FF end

    def Function_7_263B(): pass

    label("Function_7_263B")


    def lambda_2640():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFF6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2640)

    def lambda_2655():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2655)
    WaitChrThread(0xFE, 2)

    def lambda_2666():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2666)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0x13, 2)
    Return()

    # Function_7_263B end

    def Function_8_2677(): pass

    label("Function_8_2677")

    OP_68(-4000, 1950, -6700, 800)
    MoveCamera(21, 12, -1, 800)
    OP_6F(0x79)
    OP_68(-4650, 1950, -8700, 800)
    OP_6F(0x79)
    Return()

    # Function_8_2677 end

    def Function_9_26A9(): pass

    label("Function_9_26A9")

    OP_68(17070, 10650, -6540, 0)
    MoveCamera(48, 5, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(7630, 0)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1300)
    OP_68(17070, 10650, -6540, 1650)
    MoveCamera(312, 24, 0, 1650)
    OP_6E(810, 1650)
    SetCameraDistance(7630, 1650)
    Sound(914, 0, 100, 0)
    Sound(251, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xE5, 0xEF, 0x0, 0x0)
    CloseMessageWindow()
    OP_96(0xFE, 0x3A98, 0x1B58, 0xFFFFF8B2, 0x4268, 0x0)
    OP_74(0x0, 0x1E)
    OP_68(9820, 9950, -1820, 0)
    MoveCamera(82, 49, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(12750, 0)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(990, 0, 100, 0)
    OP_68(9820, 1350, -1820, 1500)
    MoveCamera(67, 7, 0, 1500)
    OP_6E(810, 1500)
    SetCameraDistance(10570, 1500)

    def lambda_27F9():
        OP_9D(0xFE, 0x29F4, 0xFFFFFE0C, 0xFFFFF8B2, 0x96, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27F9)
    Sleep(1100)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    WaitChrThread(0xFE, 2)
    OP_0D()
    Sound(833, 0, 100, 0)
    StopEffect(0x0, 0x2)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    OP_82(0x96, 0x12C, 0x1388, 0x320)
    OP_71(0x0, 0xF0, 0xF8, 0x0, 0x0)
    Sleep(300)
    CancelBlur(900)
    OP_79(0x0)
    Sleep(900)
    OP_68(9820, 2750, -1820, 600)
    MoveCamera(67, -3, 0, 600)
    OP_6E(810, 600)
    SetCameraDistance(10570, 600)
    OP_74(0x0, 0xF)
    Sound(251, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    OP_71(0x0, 0xF9, 0x104, 0x0, 0x0)

    def lambda_2921():
        OP_9C(0xFE, 0x32, 0x0, 0x0, 0x546, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2921)
    WaitChrThread(0xFE, 2)
    Sound(893, 0, 50, 0)
    OP_68(8900, 2000, -1790, 700)
    MoveCamera(61, -2, 0, 700)
    OP_6E(810, 700)
    SetCameraDistance(10360, 700)
    OP_79(0x0)
    OP_71(0x0, 0x105, 0x118, 0x0, 0x0)
    Sleep(200)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    OP_6F(0x79)
    Return()

    # Function_9_26A9 end

    def Function_10_29B0(): pass

    label("Function_10_29B0")

    Fade(100)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x40, 0x4C, 0x0, 0x0)
    OP_79(0x0)
    OP_0D()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11950, 500)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x4D, 0x55, 0x0, 0x20)
    Sleep(300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(1800)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_6F(0x79)
    CancelBlur(0)
    OP_71(0x0, 0x56, 0x63, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    Return()

    # Function_10_29B0 end

    def Function_11_2A37(): pass

    label("Function_11_2A37")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0xD4, 0xE4, 0x0, 0x0)
    Sleep(300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(400)
    CancelBlur(300)
    OP_79(0x0)
    SetChrFlags(0xFE, 0x4)
    OP_71(0x0, 0xE5, 0xED, 0x0, 0x20)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x64, 0xBB8, 0x1F4)
    Sound(251, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_68(-2700, 2550, -4100, 700)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_9C(0xFE, 0xFFFFE890, 0x1F4, 0x0, 0x226, 0x640)
    CancelBlur(0)
    Return()

    # Function_11_2A37 end

    def Function_12_2B00(): pass

    label("Function_12_2B00")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_2B00 end

    def Function_13_2B09(): pass

    label("Function_13_2B09")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_2B09 end

    def Function_14_2B12(): pass

    label("Function_14_2B12")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_2B12 end

    def Function_15_2B1B(): pass

    label("Function_15_2B1B")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2B1B end

    def Function_16_2B24(): pass

    label("Function_16_2B24")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2B24 end

    def Function_17_2B2D(): pass

    label("Function_17_2B2D")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2B2D end

    def Function_18_2B36(): pass

    label("Function_18_2B36")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch13700.itc", 0x22)
    LoadChrToIndex("chr/ch27200.itc", 0x23)
    LoadChrToIndex("chr/ch27300.itc", 0x24)
    LoadChrToIndex("chr/ch02400.itc", 0x25)
    LoadChrToIndex("chr/ch43150.itc", 0x26)
    LoadChrToIndex("chr/ch43250.itc", 0x27)
    LoadChrToIndex("chr/ch43350.itc", 0x28)
    LoadChrToIndex("apl/ch50011.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch00550.itc", 0x2E)
    LoadChrToIndex("chr/ch03550.itc", 0x30)
    LoadChrToIndex("chr/ch03552.itc", 0x31)
    LoadChrToIndex("apl/ch51408.itc", 0x32)
    LoadChrToIndex("chr/ch00053.itc", 0x33)
    LoadChrToIndex("chr/ch00153.itc", 0x34)
    LoadChrToIndex("chr/ch00253.itc", 0x35)
    LoadChrToIndex("chr/ch00353.itc", 0x36)
    LoadChrToIndex("chr/ch00056.itc", 0x39)
    LoadChrToIndex("chr/ch00156.itc", 0x3A)
    LoadChrToIndex("chr/ch00256.itc", 0x3B)
    LoadChrToIndex("chr/ch00356.itc", 0x3C)
    LoadChrToIndex("chr/ch00556.itc", 0x3D)
    LoadChrToIndex("chr/ch43100.itc", 0x3F)
    LoadChrToIndex("chr/ch43200.itc", 0x40)
    LoadChrToIndex("chr/ch43300.itc", 0x41)
    LoadChrToIndex("apl/ch51415.itc", 0x42)
    LoadChrToIndex("apl/ch51416.itc", 0x37)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00701.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    LoadEffect(0x1, "battle/bs000001.eff")
    LoadEffect(0x2, "eff/cutin35.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/ev14016.eff")
    LoadEffect(0x5, "event/ev10007.eff")
    LoadEffect(0x6, "event/ev10002.eff")
    LoadEffect(0x7, "battle/ms00001.eff")
    LoadEffect(0x8, "event/ev10006.eff")
    LoadEffect(0x9, "event/ev14015.eff")
    SoundLoad(3890)
    SoundLoad(3891)
    SoundLoad(3892)
    SoundLoad(4053)
    SoundLoad(4054)
    SoundLoad(4068)
    SoundLoad(3459)
    SoundLoad(3460)
    SoundLoad(2915)
    SoundLoad(3519)
    SoundLoad(3248)
    SoundLoad(3249)
    SoundLoad(4135)
    SoundLoad(959)
    SoundLoad(803)
    SoundLoad(825)
    RemoveParty(0x5, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD2")
    LoadChrToIndex("chr/ch02950.itc", 0x2F)
    LoadChrToIndex("chr/ch02953.itc", 0x38)
    LoadChrToIndex("chr/ch0295F.itc", 0x3E)
    SetScenarioFlags(0x0, 0)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_2DEB")

    label("loc_2DD2")

    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03053.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x3E)
    ClearScenarioFlags(0x0, 0)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_2DEB")

    OP_68(-1820, 1450, 3350, 0)
    MoveCamera(153, 15, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17390, 0)
    SetChrPos(0x101, -2190, -750, -670, 270)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x102, -210, -750, -3260, 270)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x103, -1200, -750, -2190, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x104, -2960, -750, -2640, 270)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0xF4, 960, -750, -1430, 270)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x5, 10000, 12000, -7000, 0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrPos(0xB, 200, -750, 0, 270)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 200, -750, -3000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 180)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrPos(0xF, 900, -750, -23000, 0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrPos(0xD, -900, -750, -25000, 0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrPos(0xE, 900, -750, -25000, 0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x26)
    SetChrPos(0x10, 0, -750, -13600, 0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x27)
    SetChrPos(0x11, 3850, -750, -7000, 250)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x28)
    SetChrPos(0x12, -4180, -750, -8370, 117)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x13)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -9950, -750, 880, 0)
    OP_93(0x13, 0x64, 0x0)
    OP_74(0x0, 0x1E)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 600, 750, 5200, 180)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x1000)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x1)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetScenarioFlags(0x0, 1)
    OP_68(-5390, 2150, 1420, 0)
    MoveCamera(246, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(14170, 0)
    SetCameraDistance(19170, 3000)
    FadeToBright(1000, 0)
    OP_82(0x0, 0x32, 0x5DC, 0x1388)
    BeginChrThread(0x13, 3, 0, 19)
    OP_0D()
    Sleep(500)
    Sound(843, 0, 100, 0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    PlayEffect(0x1, 0x0, 0x13, 0x1, 500, -750, 500, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_6F(0x79)
    OP_75(0x0, 0x1, 0x5DC)

    def lambda_315E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_315E)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    CancelBlur(2000)
    OP_6F(0x79)
    Sleep(500)
    OP_68(1240, 2150, 1060, 2000)
    MoveCamera(246, 16, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(15170, 2000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#6PAhhh ahhh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PWe managed to bring it down somehow..\x02",
    )

    CloseMessageWindow()
    Sound(971, 0, 100, 0)
    Sleep(1000)
    Sound(4124, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        "#04809F#5PUhufu, you do not do it well enough\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(1140, 2150, 4290, 2000)
    MoveCamera(313, 15, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9710, 2000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_326F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_326F)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_3287():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3287)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_329F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_329F)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_32B7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_32B7)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)

    def lambda_32CF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_32CF)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)

    def lambda_32E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_32E7)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xB, 2)

    ChrTalk(
        0x8,
        (
            "#04704F#5PFor hum, amateur\x01",
            "It is quite a place.\x02\x03",
            "#04700FWith that magician as well\x01",
            "As the Foundation guys made it\x01",
            "It seems that perfection is also high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#6P#N…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00311F#6P#NYou guys…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(9290, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_9B(0x1, 0x101, 0x0, 0x190, 0x3E8, 0x0)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P\"Eating snake\" ──\x01",
            "Let's answer soon!\x02\x03",
            "#00013FIn the land of Crosbell\x01",
            "What are you trying to do! Is it?\x02\x03",
            "#00007FNo doubt it is … …\x01",
            "I also made \"Gnostic\" newly\x01",
            "You guys are not! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#11PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PAhh..\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3604")

    ChrTalk(
        0x109,
        "#10110F#11POh you mean the leader from the hoodlum group\x02",
    )

    CloseMessageWindow()

    label("loc_3604")


    ChrTalk(
        0x9,
        (
            "#04809F#5PHaha, I turned into a devil\x01",
            "You are a bad leader.\x02\x03",
            "I was allowed to see it, though\x01",
            "It was quite a lot of playing.\x02\x03",
            "#04802FUhuh, if I go through a bit more\x01",
            "You may as well celebrate \"association\".\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F7")

    ChrTalk(
        0x105,
        "#10301F#11P…\x02",
    )

    CloseMessageWindow()

    label("loc_36F7")


    ChrTalk(
        0x101,
        (
            "#00007F#12PDo not move!\x01",
            "Let's answer the question!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04709F#1PHaha, you guys think so\x01",
            "I do not think it is reasonable … …\x02\x03",
            "#04702FWe are the \"plan\" to the last\x01",
            "I just came to check progress.\x02\x03",
            "The degree of activation of the seven anger and … …\x01",
            "Timing of \"promised day\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12P#NPromised Day…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P#NTips, how far\x01",
            "Thinking in my opinion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P….\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(8000, 1500)

    def lambda_3894():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3894)
    WaitChrThread(0xB, 1)
    Sleep(300)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12PIt sounds like words wont get through\x02\x03",
            "From here onwards with power\x01",
            "Let's have your mouth open.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00008F#6PSilver#2RIn#… ….\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_398F")

    ChrTalk(
        0x109,
        (
            "#10107F#12P… only to do so\x01",
            "There seems to be no way!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C5")

    label("loc_398F")


    ChrTalk(
        0x105,
        (
            "#10303F#12P… only to do so\x01",
            "There seems to be no road.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C5")

    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    Fade(500)
    OP_68(-970, 1050, 4590, 0)
    MoveCamera(150, 17, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(18630, 0)
    SetCameraDistance(18130, 1000)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        "#04704F#6POh well now\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04804F#6PHuh, it will be truly amazing\x01",
            "Is it impossible for all of you guys?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#04802F#12PHere for you\x01",
            "May I leave it to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PNo choice\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B0D():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3B0D)
    Sleep(50)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_9B(0x1, 0x9, 0x0, 0xFFFFFCE0, 0x3E8, 0x0)
    Sleep(300)
    Fade(500)
    OP_68(130, 1950, 4130, 0)
    MoveCamera(11, 10, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 1000)
    OP_6F(0x79)
    BeginChrThread(0xA, 0, 0, 22)
    Sleep(300)
    SetCameraDistance(13000, 500)
    BlurSwitch(0xA, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    CancelBlur(0)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)
    OP_68(-740, 2050, -670, 1200)
    SetCameraDistance(16550, 1200)
    OP_6F(0x79)
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
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P#NA spear…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#12P#NIt was used by medieval knights\x01",
            "Cavalry Spear#6RRun#It looks like … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NCome on … …\x01",
            "Take out such antiques\x01",
            "What is it supposed to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3890V#5P#30WNo need for questions\x02\x03",
            "#3891VBecause I took each other's gifts\x01",
            "You should hit it with all your strength.\x02\x03",
            "#3892VOtherwise you'll die\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF34)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        "#00005F#6P#NAh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#12P#NComing!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(800)
    BeginChrThread(0xA, 3, 0, 24)
    Sleep(700)
    EndChrThread(0xA, 0x3)
    BeginChrThread(0xA, 3, 0, 25)
    BeginChrThread(0x14, 1, 0, 39)
    Fade(500)
    OP_68(-4770, 1950, -2610, 0)
    OP_68(-5000, 1850, -2610, 3000)
    MoveCamera(51, 8, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(9500, 0)
    SetCameraDistance(11000, 3000)
    Fade(500)
    CancelBlur(0)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x32, 0x5DC, 0x7D0)
    SetCameraDistance(12000, 3000)
    BeginChrThread(0xB, 3, 0, 32)
    BeginChrThread(0xB, 2, 0, 33)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x101, 2, 0, 34)
    BeginChrThread(0x102, 3, 0, 28)
    BeginChrThread(0x103, 3, 0, 29)
    BeginChrThread(0x104, 3, 0, 30)
    BeginChrThread(0xF4, 3, 0, 31)

    ChrTalk(
        0x102,
        "#00105F#11P#7AEh\x02",
    )

    Sleep(800)

    ChrTalk(
        0x101,
        "#00010F#4P#N#7AAh\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)
    Sleep(300)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-3210, 1650, -4260, 1000)
    MoveCamera(36, 5, -1, 1000)
    OP_6E(530, 1000)
    SetCameraDistance(17220, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)
    Sound(369, 0, 100, 0)
    Sound(196, 0, 80, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2031, 255, 100, 0)
    Sound(2129, 255, 70, 1)
    Sound(2223, 255, 100, 2)
    Sound(2318, 255, 100, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4043")
    Sound(2464, 255, 100, 4)
    Jump("loc_4049")

    label("loc_4043")

    Sound(2404, 255, 100, 4)

    label("loc_4049")

    WaitChrThread(0xB, 2)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0xF4, 3)
    CancelBlur(0)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 26)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P…\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_412B")

    ChrTalk(
        0x109,
        "#10108F#12P#30W#NNo way that was\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#12P#30W#NCho, an ultra-fast thrust\x01",
            "Did you release dozens in an instant …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_41A4")

    label("loc_412B")


    ChrTalk(
        0x104,
        "#00310F#12P#30W#NGood … … No way … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10310F#12P#30W#N…… Super fast pick\x01",
            "Did you release dozens of ten breaths …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_41A4")


    ChrTalk(
        0x103,
        (
            "#00206F#12P#30W#N……impossible……\x01",
            "With human beings ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00710F#11P#30WUgh\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04702F#5PHo, \"steel#2RGlasses#The Spirit of the \"Saint's\"\x01",
            "I do not think there are human beings that will surpass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04809F#5PUhufu, a devil from the eastern people street\x01",
            "It seems there is only to be called?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PNot a bad reaction\x02\x03",
            "But compared with the \"previous generation\"\x01",
            "It seems that there is still hesitation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2617, 255, 100, 0)

    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00705F#11P#30W#10AWhat…\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(972, 0, 100, 0)
    Sleep(800)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-90, 550, -3200, 0)
    MoveCamera(168, 27, -1, 0)
    MoveCamera(168, 23, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1000)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x39)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 0x3A)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x3C)
    SetChrSubChip(0x104, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    ClearChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x103, 0x3B)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0xF4, 0x20)
    SetChrChipByIndex(0xF4, 0x3E)
    SetChrSubChip(0xF4, 0x0)
    Sleep(300)
    OP_6F(0x79)
    OP_FD(0xC, 0xB)
    BeginChrThread(0xB, 0, 0, 40)
    WaitChrThread(0xB, 0)
    SetChrChipByIndex(0xC, 0x42)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        "#30W…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00011F#12P…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11PWha\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PRixia….\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4602")

    ChrTalk(
        0x109,
        "#10111F#5PWell, yeah … ….?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_4602")


    ChrTalk(
        0x105,
        (
            "#10301F#5PAmazing\x01",
            "Did you change the sign ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4633")

    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#04809F#5POh this is something else!\x02\x03",
            "\"Silver#2RIn#The identity of \"\x01",
            "Alkane Shell's semi-heroine,\x01",
            "It was Risha Mao!\x02\x03",
            "#04802FUhufu, that is funny\x01",
            "Is not there a drama?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00711F#5PUgh\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x5, -900, -750, -23000, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_47B4")

    NpcTalk(
        0x105,
        "Voice of a boy",
        (
            "#2915V#6P#25A── No, no.\x01",
            "You seem to have come to a great scene.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_47EC")

    label("loc_47B4")


    NpcTalk(
        0x109,
        "Daughter's voice",
        "#3519V#6P#20AEveryone, are you ok?!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    label("loc_47EC")

    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x5)
    OP_68(-2330, 1950, -1820, 1500)
    MoveCamera(158, 16, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(14070, 1500)
    Sleep(500)

    def lambda_48C4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_48C4)
    Sleep(100)

    def lambda_48DC():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_48DC)
    Sleep(50)

    def lambda_48F4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_48F4)
    Sleep(50)

    def lambda_490C():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_490C)

    def lambda_4921():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4921)
    Sleep(50)

    def lambda_4931():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4931)
    Sleep(50)

    def lambda_4941():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_4941)
    Sleep(50)

    def lambda_4951():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4951)
    Sleep(50)

    def lambda_4961():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4961)
    Sleep(150)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_49DB")

    ChrTalk(
        0x101,
        (
            "#00008F#6P#NWadi\x01",
            "And also Arios …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A14")

    label("loc_49DB")


    ChrTalk(
        0x101,
        (
            "#00008F#6P#NNoel …\x01",
            "And also Arios …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A14")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00106F#6PSo you're here\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_4A45():
        OP_9B(0x0, 0xFE, 0x163, 0x1A90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4A45)
    Sleep(100)

    def lambda_4A5D():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4A5D)
    Sleep(150)

    def lambda_4A75():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4A75)
    Sleep(50)

    def lambda_4A8D():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A8D)
    Sleep(400)
    Fade(500)
    SetChrChipByIndex(0xC, 0x42)
    SetChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x1)
    OP_68(-3310, 1950, -11270, 0)
    MoveCamera(24, 9, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(13150, 0)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#12PThose guys are…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#12PThe Snake..\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xF,
        (
            "#4053V#11P#40WCampanella the Clown\x02\x03",
            "#4054VAlso, to the manager of \"13 studio\"\x01",
            "\"Steel's Saint\"? …\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD6)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    ChrTalk(
        0x8,
        (
            "#04705F#5P#NI see……\x01",
            "Is that \"sword of the wind\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#04802F#5P#NUhufu comparable to Levee\x01",
            "It seems to be good, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N─ ─ \"Sword of the Wind\".\x01",
            "You see#2RMami#Is it the first time you can do it?\x02\x03",
            "Indeed, no different from rumors\x01",
            "It sounds like a great skill.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#01403F#11PNo need for flattery\x02\x03",
            "As you like \"people's area\"\x01",
            "It has not been reached until it exceeds.\x02\x03",
            "#01401FEspecially in front of \"that spear\"\x01",
            "I will have no choice but to withdraw even the Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#NHuff, even if you can see it\x01",
            "It is a big deal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        "#6PArios…?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PYoyo …\x01",
            "Do not you miss it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F#11PNo way ….\x01",
            "However, the situation is disadvantageous here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P!?\x02",
    )

    CloseMessageWindow()
    OP_68(30, 150, -9540, 1500)
    MoveCamera(24, 25, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(21930, 1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(30, 150, -9540, 0)
    MoveCamera(345, 34, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(21930, 0)
    OP_68(970, 150, -9750, 3000)
    MoveCamera(64, 29, -1, 3000)
    OP_6E(530, 3000)
    SetCameraDistance(21930, 3000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x14, 1, 0, 42)
    PlayEffect(0x5, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4FF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4FF6)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5041)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_508C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_508C)
    Sleep(800)
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
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_516C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_516C)
    Sleep(150)

    def lambda_517C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_517C)
    Sleep(150)

    def lambda_518C():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_518C)
    Sleep(250)

    ChrTalk(
        0x10,
        "#11P…..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PUgh…\x01",
            "Lynn got together?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5231")

    ChrTalk(
        0x105,
        (
            "#10301F#11PApparently, these older sisters also\x01",
            "It looks like it is not a Tada person …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5267")

    label("loc_5231")


    ChrTalk(
        0x109,
        (
            "#10108F#11PUgh…\x01",
            "(There is no gap at all …!!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5267")

    OP_68(240, 1000, -7460, 1500)
    MoveCamera(25, 10, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(20910, 1500)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N─ ─ Good.\x01",
            "Here#2RNone#There is no need to do.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x11,
        "#11PRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PHah, understood\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PFor the will of the Master\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(805, 0, 70, 0)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x10, 0x3F)
    SetChrChipByIndex(0x11, 0x40)
    SetChrChipByIndex(0x12, 0x41)
    OP_0D()
    Sleep(300)

    def lambda_5355():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5355)
    Sleep(100)

    def lambda_536D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_536D)
    Sleep(100)

    def lambda_5385():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFD44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5385)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00010F#1PUgh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00712F#11P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#04804F#5P#NAhah, time to pull out then\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(440, 1150, 7910, 0)
    MoveCamera(30, 11, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(19660, 0)
    SetCameraDistance(18660, 1000)
    OP_6F(0x79)

    def lambda_5449():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5449)

    def lambda_5456():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5456)

    def lambda_5463():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5463)

    def lambda_5470():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5470)

    def lambda_547D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_547D)

    def lambda_548A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_548A)

    def lambda_5497():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_5497)

    def lambda_54A4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_54A4)

    def lambda_54B1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_54B1)

    ChrTalk(
        0x8,
        (
            "#04704F#5PThe degree of progress of \"plan\" and\x01",
            "I could confirm the state of the seven anger.\x02\x03",
            "#04702FHugh, I will soon\x01",
            "Let's say we go back to \"finishing\".\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 41)
    WaitChrThread(0x9, 0)
    Sound(959, 2, 100, 0)
    PlayEffect(0x6, 0x0, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x2, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#00007F#12P#NW-wait!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#01407F#12P#N…… as it is in this way\x01",
            "It can not be overlooked … …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PI will give you one warning\x02\x03",
            "In this \"plan\"\x01",
            "We are nothing but supporting persons.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P#NHuh?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#01405Fwhat#12P#N……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5PAs soon as the beasts were released,\x01",
            "This place will cause confusion.\x02\x03",
            "However, to the tragedy that happens in front of you\x01",
            "Make sure you do not get caught too much.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#04802F#5PUhufu …\x01",
            "Well then, I'm in love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04709F#5PHaha, I will see you again\x01",
            "Please look forward to it.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 35)
    BeginChrThread(0x102, 1, 0, 35)
    BeginChrThread(0x103, 1, 0, 35)
    BeginChrThread(0x104, 1, 0, 35)
    BeginChrThread(0xF4, 1, 0, 35)
    ClearChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    Sound(4135, 255, 100, 0)
    OP_68(-160, 750, 1070, 8000)
    MoveCamera(31, 15, -1, 8000)
    OP_6E(530, 8000)
    SetCameraDistance(25510, 8000)
    StopEffect(0x0, 0x2)

    def lambda_586E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_586E)
    Sound(1035, 0, 100, 0)
    Sound(977, 0, 100, 0)
    Sleep(400)
    StopEffect(0x1, 0x2)

    def lambda_5891():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5891)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopEffect(0x2, 0x2)

    def lambda_58AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_58AE)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopSound(959, 1000, 100)
    Sleep(600)

    def lambda_58D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_58D1)
    Sleep(400)

    def lambda_58E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_58E5)
    Sleep(400)

    def lambda_58F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_58F9)
    Sleep(400)
    StopBGM(0x1F40)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xC)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xD)
    OP_64(0xE)
    OP_64(0xF)
    OP_6F(0x79)
    Fade(500)
    OP_68(-860, 750, -6060, 0)
    MoveCamera(137, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17680, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xE,
        "#11PUgh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P\"Eating snake\" … …\x01",
            "They are outrageous people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00713F#11P#40W….\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 3, 0, 36)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x102, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 38)
    BeginChrThread(0x109, 3, 0, 38)
    BeginChrThread(0x105, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 38)
    BeginChrThread(0xE, 3, 0, 38)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xE, 2)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00011F#12PRixia…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PRixia-san…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        (
            "#00714F#3248V#5P#30W…. Soon so I will practice\x01",
            "Because I have to go back.\x02\x03",
            "#00713F#3249VExcuse me…\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCB1)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0xC, 3, 0, 37)
    Sleep(500)
    OP_68(2660, 750, -9640, 2000)
    MoveCamera(140, 15, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(23490, 2000)
    WaitChrThread(0xC, 3)
    SetChrFlags(0xC, 0x80)
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_68(-960, 750, -5650, 1500)
    MoveCamera(140, 17, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(18220, 1500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00008F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PJust incredibly happening\x01",
            "I do not feel a little reality …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PYeah…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PIt's like being in a dream\x01",
            "I am in the mood ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PR-really…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#12PGood thing with Wald … …\x01",
            "I think it is kind of a nightmare.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xF,
        "#01403F#4068V#5P#40WBut this is reality for sure\x02",
    )

    CloseMessageWindow()
    OP_24(0xFE4)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5FA6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5FA6)
    Sleep(50)

    def lambda_5FB6():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FB6)

    def lambda_5FC3():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FC3)
    Sleep(50)

    def lambda_5FD3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5FD3)

    def lambda_5FE0():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FE0)

    def lambda_5FED():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FED)
    Sleep(50)

    def lambda_5FFD():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FFD)

    def lambda_600A():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_600A)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)

    ChrTalk(
        0x101,
        "#00001F#6PArios…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#01401F#5PThose of \"association\" are more than expected\x01",
            "He left a clue.\x02\x03",
            "The meaning of this place, and\x01",
            "\"Beasts to be released soon\" … …\x02\x03",
            "#01403FWe don't have time to be surprised\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#6PRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#12PBeasts… no way\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
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

    def lambda_61D1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61D1)

    def lambda_61DE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_61DE)
    Sleep(50)

    def lambda_61EE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_61EE)

    def lambda_61FB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_61FB)
    Sleep(50)

    def lambda_620B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_620B)

    def lambda_6218():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6218)
    Sleep(50)

    def lambda_6228():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6228)

    def lambda_6235():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6235)
    Sleep(700)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00011F#6PIs that so?\x01",
            "A guide wave arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F#11PYes, barely\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F── Yes!\x01",
            "It is Bunnings, Division Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3459V#30WThis is Dudley\x02\x03",
            "#3460VI heard that it went to the south shore of the lake\x01",
            "Now, are you there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD84)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FAh, yes\x02\x03",
            "#00001FThat … … there are various things\x01",
            "Arios are also with us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then exactly fine.\x01",
            "In addition, please also tell them.\x02\x03",
            "─ ─ Members of the \"red constellation\"\x01",
            "Every single person disappeared from the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F#4SWHAT!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If possible from Orlando\x01",
            "I want to hear the story.\x02\x03",
            "Can you get back here right away?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010FU-understood\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101F#5PWhat happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10113F#5PYou had quite a reaction there\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00003F#6PYeah…\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd relayed the info from Dudley\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x104,
        "#00310F#4S#11P!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PThat is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PRed Constellation…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PCut …\x01",
            "We were also concerned.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#01403F#5P── Lloyd.\x01",
            "You hurry back to the city.\x02\x03",
            "#01400FWe, this place\x01",
            "Let's examine it and return.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_6856():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6856)
    Sleep(50)

    def lambda_6866():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6866)

    def lambda_6873():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6873)
    Sleep(50)

    def lambda_6883():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6883)

    def lambda_6890():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6890)

    def lambda_689D():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_689D)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#00011F#6PAhh..\x02\x03",
            "#00003F……Excuse me.\x01",
            "I will be saved if you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12PSorry…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PWe have to work together at times like this\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAlso, with phosphorus and aeolia\x01",
            "I will not be able to move right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#01403F#5PIf \"red constellation\" moved\x01",
            "There must be movement of \"Black moon\" ……\x02\x03",
            "#01401FWe also return soon\x01",
            "Be careful, be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PExcuse us!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20180, 2000)
    StopSound(122, 2000, 50)
    StopSound(123, 2000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x0, 0x10000)
    OP_24(0x323)
    SoundLoad(959)
    SoundLoad(825)
    SetScenarioFlags(0x22, 1)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2B36 end

    def Function_19_6A7E(): pass

    label("Function_19_6A7E")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x0)
    OP_79(0x0)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_19_6A7E end

    def Function_20_6AA0(): pass

    label("Function_20_6AA0")

    Sound(970, 0, 100, 0)
    Sound(920, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(893, 0, 70, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(156)
    SetChrSubChip(0xFE, 0x9)
    Sleep(144)
    SetChrSubChip(0xFE, 0xA)
    Sleep(132)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(108)
    SetChrSubChip(0xFE, 0xD)
    Sleep(96)
    SetChrSubChip(0xFE, 0xE)
    Sleep(84)
    SetChrSubChip(0xFE, 0xF)
    Sleep(72)

    label("loc_6B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B8C")
    Sound(893, 0, 50, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(60)
    SetChrSubChip(0xFE, 0x9)
    Sleep(60)
    SetChrSubChip(0xFE, 0xA)
    Sleep(60)
    SetChrSubChip(0xFE, 0xB)
    Sleep(60)
    SetChrSubChip(0xFE, 0xC)
    Sleep(60)
    SetChrSubChip(0xFE, 0xD)
    Sleep(60)
    SetChrSubChip(0xFE, 0xE)
    Sleep(60)
    SetChrSubChip(0xFE, 0xF)
    Sleep(60)
    Jump("loc_6B3A")

    label("loc_6B8C")

    Sound(893, 0, 60, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(72)
    SetChrSubChip(0xFE, 0x9)
    Sleep(84)
    SetChrSubChip(0xFE, 0xA)
    Sleep(96)
    SetChrSubChip(0xFE, 0xB)
    Sleep(108)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xD)
    Sleep(132)
    SetChrSubChip(0xFE, 0xE)
    Sleep(144)
    SetChrSubChip(0xFE, 0xF)
    Sleep(156)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 50, 0)
    Sound(308, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(400)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_6AA0 end

    def Function_21_6BEC(): pass

    label("Function_21_6BEC")

    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1F4, 0x1)
    Return()

    # Function_21_6BEC end

    def Function_22_6BFF(): pass

    label("Function_22_6BFF")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 60, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 20)
    BeginChrThread(0x15, 2, 0, 21)
    Sleep(2500)
    ClearScenarioFlags(0x0, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x15, 3)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(3000)
    OP_82(0x0, 0x64, 0x1388, 0x320)
    SetCameraDistance(11000, 250)

    def lambda_6C9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6C9E)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    Sound(288, 0, 70, 0)
    Sound(308, 0, 100, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Return()

    # Function_22_6BFF end

    def Function_23_6CF4(): pass

    label("Function_23_6CF4")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(150)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(800)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    Return()

    # Function_23_6CF4 end

    def Function_24_6D5E(): pass

    label("Function_24_6D5E")

    SetChrChipByIndex(0xFE, 0x31)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_24_6D5E end

    def Function_25_6D7D(): pass

    label("Function_25_6D7D")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_6D95():
        OP_9D(0xFE, 0xFFFFFF06, 0xFFFFFD12, 0x726, 0x96, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D95)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x4, 0x0, 0xFE, 0x4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    StopEffect(0x0, 0x2)
    Return()

    # Function_25_6D7D end

    def Function_26_6E8E(): pass

    label("Function_26_6E8E")

    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 60, 0)
    Sound(250, 0, 80, 0)

    def lambda_6EAE():
        OP_9D(0xFE, 0x258, 0xFA, 0x1900, 0x60E, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6EAE)
    WaitChrThread(0xFE, 2)
    Sound(326, 0, 50, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(531, 0, 60, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    Return()

    # Function_26_6E8E end

    def Function_27_6EFA(): pass

    label("Function_27_6EFA")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    label("loc_6F02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F29")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_6F02")

    label("loc_6F29")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(251, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0xFFFFFE70, 0xFFFFF34E, 0x2EE, 0x3AB6)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_27_6EFA end

    def Function_28_6FA6(): pass

    label("Function_28_6FA6")

    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    label("loc_6FAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD5")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_6FAE")

    label("loc_6FD5")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFA, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_28_6FA6 end

    def Function_29_7046(): pass

    label("Function_29_7046")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_704E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7075")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_704E")

    label("loc_7075")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFEF66, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_29_7046 end

    def Function_30_70E6(): pass

    label("Function_30_70E6")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    label("loc_70EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7115")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_70EE")

    label("loc_7115")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFFFFFF06, 0x0, 0xFFFFF15A, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_30_70E6 end

    def Function_31_718C(): pass

    label("Function_31_718C")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)

    label("loc_7194")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71BB")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_7194")

    label("loc_71BB")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x190, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_31_718C end

    def Function_32_722C(): pass

    label("Function_32_722C")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xDAC, 0x0, 0xFFFFFE0C, 0x3E8, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xFFFFF060, 0x0, 0x0, 0x5DC, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0xC8, 0xBB8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)

    label("loc_7293")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72AA")
    Sleep(1)
    Jump("loc_7293")

    label("loc_72AA")

    Sleep(200)
    OP_9D(0xFE, 0xC8, 0xFFFFFD12, 0xFFFFF3E4, 0x2EE, 0x5DC)
    Return()

    # Function_32_722C end

    def Function_33_72C5(): pass

    label("Function_33_72C5")

    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_33_72C5 end

    def Function_34_73FD(): pass

    label("Function_34_73FD")

    Sleep(50)
    PlayEffect(0x7, 0xFF, 0x101, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x7, 0xFF, 0x102, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x7, 0xFF, 0x103, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x7, 0xFF, 0x104, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x7, 0xFF, 0xF4, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_34_73FD end

    def Function_35_7520(): pass

    label("Function_35_7520")

    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_7520 end

    def Function_36_7533(): pass

    label("Function_36_7533")

    OP_93(0xFE, 0xB3, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x514, 0x4B0, 0x0)
    OP_95(0xFE, 470, -750, -5220, 1200, 0x0)
    OP_93(0xFE, 0x87, 0x0)
    Return()

    # Function_36_7533 end

    def Function_37_7568(): pass

    label("Function_37_7568")

    SetChrFlags(0xFE, 0x40)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x5, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_9B(0x0, 0xFE, 0x5, 0x9C4, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xDAC, 0x6D6, 0xFFFFDECC, 0x7D0, 0xDAC)
    ClearChrFlags(0xFE, 0x20)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0x3E8, 0xFA0, 0xFFFFF768, 0x1388, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_7568 end

    def Function_38_765A(): pass

    label("Function_38_765A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7674")
    TurnDirection(0xFE, 0xC, 500)
    Sleep(300)
    Jump("Function_38_765A")

    label("loc_7674")

    Return()

    # Function_38_765A end

    def Function_39_7675(): pass

    label("Function_39_7675")

    Sleep(200)
    Sound(287, 0, 100, 0)
    Sound(270, 0, 80, 0)
    Sound(225, 0, 70, 0)
    Sound(833, 0, 70, 0)
    Sound(825, 2, 100, 0)
    Sleep(1000)
    Sound(271, 0, 80, 0)
    Sound(287, 0, 60, 0)
    Sleep(1000)
    StopSound(225, 1000, 40)
    StopSound(825, 1000, 90)
    Return()

    # Function_39_7675 end

    def Function_40_76B5(): pass

    label("Function_40_76B5")

    SetChrChipByIndex(0xFE, 0x42)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    Sound(1037, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(400)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x2)
    Sleep(400)
    Sound(1037, 0, 70, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(400)
    SetChrSubChip(0xFE, 0x4)
    Sleep(400)
    Return()

    # Function_40_76B5 end

    def Function_41_76F3(): pass

    label("Function_41_76F3")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Return()

    # Function_41_76F3 end

    def Function_42_770C(): pass

    label("Function_42_770C")

    Sleep(1500)
    Sound(936, 0, 100, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Return()

    # Function_42_770C end

    SaveToFile()

Try(main)
