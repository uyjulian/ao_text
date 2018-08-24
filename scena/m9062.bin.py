from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9062.bin",                # FileName
        "m9062",                    # MapName
        "m9062",                    # Location
        0x00C1,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 193, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9062",                  # 0
        "Wald",                   # 1
        "Demon Wald",             # 2
        "台詞表示用ダミーキャラ", # 3
        "Wald's Companion",       # 4
        "Wald's Companion",       # 5
        "bm9049",                 # 6
    ))

    ATBonus("ATBonus_154", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_214", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 13, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_224", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_200", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_204", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_208", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_20C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_234", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9049", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88301.dat", "ms81401.dat", "ms81401.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_214", "MonsterBattlePostion_1F4", "ed7540", "ed7453", "ATBonus_154"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51112.itc",                   # 00
    ))

    DeclNpc(0,       0,       38500,   270,  389,  0x0, 4,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(836, 0)                                        # 0

    ScpFunction((
        "Function_0_344",          # 00, 0
        "Function_1_3C0",          # 01, 1
        "Function_2_5C5",          # 02, 2
        "Function_3_916",          # 03, 3
        "Function_4_B96",          # 04, 4
        "Function_5_CE9",          # 05, 5
        "Function_6_D2A",          # 06, 6
        "Function_7_D67",          # 07, 7
        "Function_8_3161",         # 08, 8
        "Function_9_318C",         # 09, 9
        "Function_10_31B7",        # 0A, 10
        "Function_11_31E2",        # 0B, 11
        "Function_12_320D",        # 0C, 12
        "Function_13_3238",        # 0D, 13
        "Function_14_3263",        # 0E, 14
        "Function_15_327B",        # 0F, 15
        "Function_16_3293",        # 10, 16
        "Function_17_32AB",        # 11, 17
        "Function_18_32C9",        # 12, 18
        "Function_19_32E7",        # 13, 19
        "Function_20_3320",        # 14, 20
        "Function_21_3346",        # 15, 21
        "Function_22_335C",        # 16, 22
        "Function_23_3372",        # 17, 23
        "Function_24_33A3",        # 18, 24
        "Function_25_33EC",        # 19, 25
        "Function_26_3435",        # 1A, 26
        "Function_27_3452",        # 1B, 27
        "Function_28_3533",        # 1C, 28
        "Function_29_4B3E",        # 1D, 29
        "Function_30_4B7D",        # 1E, 30
        "Function_31_4BB5",        # 1F, 31
        "Function_32_4C00",        # 20, 32
        "Function_33_4C1C",        # 21, 33
        "Function_34_4CE8",        # 22, 34
        "Function_35_4D41",        # 23, 35
        "Function_36_4D8D",        # 24, 36
        "Function_37_4ECB",        # 25, 37
        "Function_38_4FE7",        # 26, 38
        "Function_39_5040",        # 27, 39
        "Function_40_504E",        # 28, 40
        "Function_41_510E",        # 29, 41
        "Function_42_518E",        # 2A, 42
        "Function_43_51AE",        # 2B, 43
        "Function_44_51C3",        # 2C, 44
        "Function_45_51EB",        # 2D, 45
        "Function_46_5278",        # 2E, 46
        "Function_47_5305",        # 2F, 47
        "Function_48_53AD",        # 30, 48
        "Function_49_5BCB",        # 31, 49
        "Function_50_5BE2",        # 32, 50
    ))


    def Function_0_344(): pass

    label("Function_0_344")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_355")
    Event(0, 3)

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_366")
    Event(0, 7)

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_37D")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 28)
    Jump("loc_3BF")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_391")
    ClearScenarioFlags(0x22, 1)
    Event(0, 48)
    Jump("loc_3BF")

    label("loc_391")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, -200, 38500, 225)
    SetChrSubChip(0x8, 0x0)

    label("loc_3BF")

    Return()

    # Function_0_344 end

    def Function_1_3C0(): pass

    label("Function_1_3C0")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D9")

    OP_1B(0x0, 0x0, 0x4)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_43A")
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Jump("loc_482")

    label("loc_43A")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_51C")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Jump("loc_5B8")

    label("loc_51C")

    OP_C3(0x0, 0x6, 0x3, 0x1E, 0x0, 0x1, -20000, -4000, 40000, 5000, 30000, 0)
    OP_C3(0x1, 0x6, 0x3, 0x1E, 0x0, 0x1, 20000, -4000, 40000, 5000, 30000, 0)
    OP_C3(0x2, 0x6, 0x3, 0x1E, 0x0, 0x1, 20000, -4000, 27000, 5000, 30000, 0)
    OP_C3(0x3, 0x6, 0x3, 0x1E, 0x0, 0x1, -20000, -4000, 27000, 5000, 30000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg0.eff")

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_5C4")
    Call(0, 50)

    label("loc_5C4")

    Return()

    # Function_1_3C0 end

    def Function_2_5C5(): pass

    label("Function_2_5C5")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(
        0x8,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWald... It seems he's\x01",
            "completely passed out.\x02\x03",
            "#00004FHe encouraged us just now...\x01",
            "I guess this guy isn't honest\x01",
            "with himself either, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, you're right.\x01",
            "He was also worried\x01",
            "about KeA...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIn any case, I think\x01",
            "it's best if we carry\x01",
            "him to the Merkabah...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FBut carryin' this guy\x01",
            "would be a little much,\x01",
            "even for me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_836")

    ChrTalk(
        0x105,
        (
            "#10400FWell, it should be ok if\x01",
            "I have Abbas come later\x01",
            "and help us out.\x02\x03",
            "#10403FThe surroundings seem\x01",
            "safe, so there's no need\x01",
            "to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, so it seems. Shall\x01",
            "we proceed for now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA")

    label("loc_836")


    ChrTalk(
        0x101,
        (
            "#00003FIt should be ok if I\x01",
            "have Abbas come later\x01",
            "and help us out.\x02\x03",
            "#00000FThe surroundings seem\x01",
            "safe... Shall we proceed\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BA")

    SetScenarioFlags(0x1CE, 5)
    Jump("loc_912")

    label("loc_8C2")


    ChrTalk(
        0x8,
        "............\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "He seems to have\x01",
            "completely lost\x01",
            "consciousness.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_912")

    TalkEnd(0x8)
    Return()

    # Function_2_5C5 end

    def Function_3_916(): pass

    label("Function_3_916")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-790, 1500, 43820, 0)
    MoveCamera(55, 54, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x0, 0, 0, 45000, 180)
    SetChrPos(0x1, 0, 0, 45000, 180)
    SetChrPos(0x2, 0, 0, 45000, 180)
    SetChrPos(0x3, 0, 0, 45000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A26)

    def lambda_A37():
        OP_95(0xFE, -230, 0, 42280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A37)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A8E)

    def lambda_A9F():
        OP_95(0xFE, -1220, 0, 42680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A9F)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_AFC)

    def lambda_B0D():
        OP_95(0xFE, 840, 0, 42720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B0D)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_B64)

    def lambda_B75():
        OP_95(0xFE, -2270, 0, 43450, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B75)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_916 end

    def Function_4_B96(): pass

    label("Function_4_B96")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BEF)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_C3A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_C85)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_CD0)
    Sleep(1000)
    NewScene("m9002", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_4_B96 end

    def Function_5_CE9(): pass

    label("Function_5_CE9")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D01")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_D01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D15")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_D15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D29")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_D29")

    Return()

    # Function_5_CE9 end

    def Function_6_D2A(): pass

    label("Function_6_D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3E")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_D3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D52")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_D52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D66")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_D66")

    Return()

    # Function_6_D2A end

    def Function_7_D67(): pass

    label("Function_7_D67")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01600.itp")
    LoadChrToIndex("chr/ch02150.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    SoundLoad(2921)
    SoundLoad(2922)
    SoundLoad(2923)
    SoundLoad(3580)
    SoundLoad(3581)
    SoundLoad(3582)
    SoundLoad(3583)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3A")
    Call(0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E06")
    OP_CF(0x1, 0xF5, 0x5)
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_E06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E20")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_E20")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3A")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_E3A")

    LoadChrToIndex("monster/ch81450.itc", 0x26)
    LoadChrToIndex("monster/ch81450.itc", 0x27)
    LoadChrToIndex("apl/ch51761.itc", 0x28)
    LoadEffect(0x0, "event/ev602_01.eff")
    LoadEffect(0x1, "event/ev602_02.eff")
    LoadEffect(0x2, "event/ev602_01.eff")
    LoadEffect(0x3, "event/ev17004.eff")
    LoadEffect(0x4, "event/ev17005.eff")
    LoadEffect(0x5, "event/ev14006.eff")
    SoundLoad(825)
    SoundLoad(832)
    SoundLoad(154)
    SetChrPos(0xF4, 0, 0, 11800, 0)
    SetChrPos(0x101, 900, 0, 11100, 0)
    SetChrPos(0x103, 200, 0, 10000, 0)
    SetChrPos(0x102, -900, 0, 10750, 0)
    SetChrPos(0x104, -600, 0, 9250, 0)
    SetChrPos(0xF5, 800, 0, 9000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 0, 0, 36500, 180)
    SetChrPos(0x9, 0, 0, 37000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 0, 1000, 28000, 0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x4)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, -3000, 300, 38000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x4)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, 3000, 300, 38000, 180)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xB, 2, 0, 26)
    BeginChrThread(0xC, 2, 0, 26)
    OP_68(0, 1000, 15500, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, 1000, 18000, 4500)
    MoveCamera(0, 38, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(24000, 4500)
    Sound(154, 2, 80, 0)
    FadeToBright(1000, 0)

    def lambda_1103():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1103)
    Sleep(50)

    def lambda_111B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_111B)
    Sleep(50)

    def lambda_1133():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1133)
    Sleep(50)

    def lambda_114B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_114B)
    Sleep(50)

    def lambda_1163():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1163)
    Sleep(50)

    def lambda_117B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_117B)
    OP_0D()
    Sleep(2400)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xA,
        "Youth's Voice",
        (
            "#3580V#6P#30WHeh heh... I got sick\x01",
            "and tired of waiting so\x01",
            "damn long, ya know?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDFC)
    OP_C9(0x1, 0x80000000)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    BeginChrThread(0x101, 0, 0, 9)
    BeginChrThread(0x102, 0, 0, 11)
    BeginChrThread(0x103, 0, 0, 10)
    BeginChrThread(0x104, 0, 0, 12)
    BeginChrThread(0xF4, 0, 0, 8)
    BeginChrThread(0xF5, 0, 0, 13)
    OP_68(0, -200, 32150, 4000)
    MoveCamera(0, 33, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(18390, 4000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)
    StopSound(154, 4000, 80)
    Fade(500)
    OP_68(-140, 1300, 32580, 0)
    MoveCamera(44, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16140, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        "#10401F#12P...Wald.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Hah, you even came all dressed up\x01",
            "in your work clothes and\x01",
            "everything.\x02\x03",
            "The Gralsritter... The secret unit\x01",
            "of the Church, is it?\x02",
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
        (
            "#10406F#12PMore or less.\x02\x03",
            "#10404FAlthough I personally like\x01",
            "the style I wore during my\x01",
            "time as a Testament more.\x02\x03",
            "#10402FOh, but even the suit I\x01",
            "rock when I'm a host isn't\x01",
            "too shabby either, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01604F#5PHeh... A bastard with\x01",
            "poor taste as always.\x02\x03",
            "#01602FMessing around with all\x01",
            "those side jobs made your\x01",
            "head numb, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PYou're one to talk.\x02\x03",
            "#10401FEven though you've obtained "power",\x01",
            "you still won't part with that lame\x01",
            "excuse for a wooden sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01603F#5PWhy would I? After all,\x01",
            "this little guy's my\x01",
            ""symbol".\x02\x03",
            "#01601FThat I'm not some soulless\x01",
            "being, living a lie, being\x01",
            "used by everyone, like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PAnd that's why you destroyed\x01",
            "that Downtown apartment with\x01",
            "a kick, right?\x02\x03",
            "#10400FEven to derail that train,\x01",
            "you used all your might to\x01",
            "do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01602F#5PHeh, so you knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PEven if I didn't want to\x01",
            "know, it was pretty\x01",
            "obvious to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01604F#5PHeh heh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#12PHehehe...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1929")

    ChrTalk(
        0x109,
        (
            "#10112F#12P(Regardless of what they're\x01",
            "saying, could it be that\x01",
            "they actually get along?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B4")

    label("loc_1929")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1965")

    ChrTalk(
        0x10A,
        "#00606F#12P(Hmph... Delinquents.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B4")

    label("loc_1965")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19B4")

    ChrTalk(
        0x106,
        (
            "#10710F#12P(They seem to be getting\x01",
            "along rather well...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B4")


    ChrTalk(
        0x103,
        "#00204F#12P#N(...Right.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00300F#12P#N(Well, it looks like an\x01",
            "ironically inseparable\x01",
            "relationship.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#12P............\x02",
    )

    CloseMessageWindow()

    def lambda_1A4A():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A4A)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12P─Wald. Let me confirm one\x01",
            "thing.\x02\x03",
            "#00013FWho gave you that "power"...\x01",
            "No, who gave you the Gnosis.\x01",
            "Was it Mariabell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01605F#5PAh, that blue drug?\x02\x03",
            "#01604FOh yeah, I've got a\x01",
            "feeling she blurted out\x01",
            "a name like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12PIt wasn't a red-colored\x01",
            "one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#12P#NYes, it's the red one\x01",
            "which causes one to\x01",
            ""Demonize"...\x02\x03",
            "#00201FAnd yet, how?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01602F#5PHeh. According to that woman it\x01",
            "seems I'm a good "match", you\x01",
            "know?\x02\x03",
            "I have the qualities to be able to\x01",
            "tap into my maximum "power" even\x01",
            "without using the dangerous one.\x02\x03",
            "#01604FWell, that was the reasoning\x01",
            "behind it. But I don't give a shit\x01",
            "either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12P#NThis isn't good...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#12P#NDon't tell me Bell gave\x01",
            "that drug to someone\x01",
            "else as well?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01605F#5PWell... Doesn't look that way.\x02\x03",
            "#01604FHeh, she's a mysterious bitch,\x01",
            "but personally, I don't\x01",
            "dislike that side of her.\x02\x03",
            "#01602FShe's pretty damn devoted to\x01",
            "her own ambitions, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10406F#12PSo you were tempted by\x01",
            "her sweet words...\x02\x03",
            "#10408FAnd you started desiring\x01",
            "unlimited "power".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01604F#5PHeh... Wrong.\x02\x03",
            "I've been yearning for\x01",
            ""power" ever since I was\x01",
            "a lil' brat...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(15140, 20000)
    Sound(805, 0, 50, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(350)

    def lambda_2015():
        OP_A6(0xFE, 0x0, 0xA, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2015)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#01608F#5P#30WAnd after my drunkard of an ol'\x01",
            "man croaked, I was left alone\x01",
            "on the streets of Downtown...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2139():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2139)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01603F#5P#30WBrawlin' in the streets, I\x01",
            "eventually found my "sanctuary",\x01",
            "the Vipers and Ignis...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21BC():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21BC)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01601F#30WEven when things heated up after an opponent\x01",
            "like you appeared, that desire kept\x01",
            "smouldering at the bottom of my heart...\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    Sound(817, 0, 60, 0)
    Sound(825, 2, 70, 0)
    Sound(832, 2, 100, 0)

    def lambda_2278():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2278)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00010F#12P#20AUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10410F#12P#20A............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 0, 0, 14)
    Sleep(50)
    BeginChrThread(0xF4, 0, 0, 15)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 17)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 16)
    Sleep(50)
    BeginChrThread(0x104, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 19)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Sleep(800)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x8,
        (
            "#01611F#5P#20A#4SAnd that is─ My thirst\x01",
            "for "power"!!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0x8, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 950, 35470, 0)
    MoveCamera(33, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12320, 0)
    SetCameraDistance(10000, 3200)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 27)
    Sound(889, 0, 100, 0)
    OP_0D()
    Sleep(1400)
    OP_68(0, 1700, 35470, 1000)
    WaitChrThread(0x8, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(3551, 255, 100, 0)
    SetCameraDistance(10000, 1300)
    OP_82(0xC8, 0x64, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_68(0, 3900, 35500, 900)
    SetCameraDistance(8360, 900)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sound(817, 0, 100, 0)
    OP_82(0x64, 0xC8, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_82(0xC8, 0x64, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0xFF, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1200, 2000, 1200, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0xC8, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_82(0xC8, 0x64, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_78(0x0, 0x9)
    OP_93(0x9, 0xB4, 0x0)

    def lambda_262D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_262D)
    ClearMapObjFlags(0x0, 0x4)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    Sleep(200)
    OP_87(0x5, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    CancelBlur(500)
    Sleep(300)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(700)
    StopSound(825, 1000, 70)
    StopSound(832, 1000, 100)
    OP_68(0, 2900, 33500, 0)
    MoveCamera(332, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13250, 0)
    MoveCamera(28, 11, 0, 4000)
    Fade(500)
    OP_71(0x0, 0x44C, 0x460, 0x0, 0x20)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_6F(0x79)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(1000)
    SetChrPos(0x8, 0, 0, 35500, 180)
    SetChrPos(0x9, 0, 0, 35500, 180)
    OP_68(-970, 2200, 31180, 0)
    MoveCamera(40, 6, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12730, 0)
    SetCameraDistance(14730, 2000)
    BeginChrThread(0x9, 3, 0, 23)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00208F#12P#N...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2856")

    ChrTalk(
        0x109,
        (
            "#10110F#12P#NGuh... The one... from\x01",
            "back then!?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_28D1")

    label("loc_2856")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_288D")

    ChrTalk(
        0x106,
        "#10712F#12P#N...The "Ogre"!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_28D1")

    label("loc_288D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28D1")

    ChrTalk(
        0x10A,
        (
            "#00610F#12P#NThis is what was in the\x01",
            "reports!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_28D1")

    BeginChrThread(0x9, 3, 0, 20)
    Sleep(2000)
    SetMessageWindowPos(20, -1, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40WHEH... COME NOW, IT'S\x01",
            "YOUR TURN TO SHOW ME...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40WYOUR THIRST FOR "POWER"...\x01",
            "...THE PROOF THAT YOU AND\x01",
            "I ARE THE SAME!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(0, 2100, 31770, 0)
    MoveCamera(138, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12500, 0)
    SetChrPos(0x8, 0, 0, 36500, 180)
    SetChrPos(0x9, -500, 0, 36500, 180)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10406F#11P...Very well.\x02\x03",
            "#10408FHowever... Mine is not\x01",
            "the same as yours.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x1D7, 0x1E0, 0x1, 0x0)
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(500)
    SetMessageWindowPos(50, 100, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40WWHAT!?\x07\x00\x02",
        )
    )

    OP_79(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(895, 0, 50, 0)
    PlayEffect(0x3, 0x1, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(832, 2, 100, 0)
    PlayEffect(0x4, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PThis is...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BCB")

    ChrTalk(
        0x109,
        (
            "#10105F#5PA golden-\x01",
            "colored...pattern...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF0")

    label("loc_2BCB")


    ChrTalk(
        0x104,
        "#00305F#11PA golden... pattern?\x02",
    )

    CloseMessageWindow()

    label("loc_2BF0")


    ChrTalk(
        0x102,
        "#00101F#11PStigma!\x02",
    )

    CloseMessageWindow()
    Sound(895, 0, 70, 0)
    StopEffect(0x1, 0x2)
    PlayEffect(0x3, 0x3, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x2, 0x2)
    PlayEffect(0x4, 0x4, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    SetCameraDistance(11000, 8000)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#10403F#11P#30WBecause this mark appeared...\x01",
            "I obtained everything, and\x01",
            "lost everything.\x02\x03",
            "Family, homeland, future...\x01",
            "everything...\x02\x03",
            "#10408FI live a fabricated life\x01",
            "combining "power" with\x01",
            "continuous despair...\x02\x03",
            "#10401FThat is "me"─ Wazy\x01",
            "Hemisphere.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 100, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W...YOU...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    SetChrPos(0x8, 0, 0, 36500, 180)
    SetChrPos(0x9, 0, 0, 36500, 180)
    OP_68(-50, 1800, 30300, 0)
    MoveCamera(359, 5, -1, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(13000, 30000)
    Sleep(300)
    Sound(895, 0, 100, 0)
    Sound(223, 0, 100, 0)
    StopEffect(0x3, 0x2)
    PlayEffect(0x3, 0x1, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x4, 0x2)
    PlayEffect(0x4, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x105,
        "Dominion Wazy",
        (
            "#10403F#2921V#6P#N#45A#30W─Dominion No. IX, the\x01",
            "Azure Testament, Wazy\x01",
            "Hemisphere...\x02\x03",
            "#2922V#42AWith this golden-colored\x01",
            "radiance, I will break\x01",
            "your "power".\x02\x03",
            "#10400F#2923V#20A─Are you prepared?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3F2, 0x3FC, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 22)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3581V#4S#30A#30WGYAHAHA, EXCELLENT!\x07\x00\x02",
        )
    )

    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 24)
    Sleep(100)
    BeginChrThread(0xC, 3, 0, 25)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3582V#4S#50W#40ABY DEVOURING YOU AS A\x01",
            "SACRIFICE, MY "POWER"\x01",
            "WILL BE COMPLETE!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(532, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x83, 0x8C, 0x1, 0x0)
    Sleep(1000)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#35A#3583V#5S#50WCOME... LET'S SETTLE\x01",
            "THIIISSS!!\x07\x00\x02",
        )
    )

    Sleep(2000)
    OP_82(0xC8, 0xC8, 0xBB8, 0x9C4)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDFF)
    OP_C9(0x1, 0x80000000)
    Sound(893, 0, 100, 0)
    Sound(892, 0, 100, 0)
    Sound(833, 0, 50, 0)
    OP_71(0x0, 0x8D, 0x90, 0x1, 0x0)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(450)
    CancelBlur(500)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_234", 0x30200011, 0x0, 0x100, 0x1D, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 28)
    OP_37()
    Return()

    # Function_7_D67 end

    def Function_8_3161(): pass

    label("Function_8_3161")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0x7364, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_8_3161 end

    def Function_9_318C(): pass

    label("Function_9_318C")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x0, 0x6E28, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_318C end

    def Function_10_31B7(): pass

    label("Function_10_31B7")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x0, 0x68F6, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_31B7 end

    def Function_11_31E2(): pass

    label("Function_11_31E2")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x0, 0x6BB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_31E2 end

    def Function_12_320D(): pass

    label("Function_12_320D")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x0, 0x6E1E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_320D end

    def Function_13_3238(): pass

    label("Function_13_3238")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x0, 0x6D56, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_3238 end

    def Function_14_3263(): pass

    label("Function_14_3263")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_3263 end

    def Function_15_327B(): pass

    label("Function_15_327B")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_327B end

    def Function_16_3293(): pass

    label("Function_16_3293")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_3293 end

    def Function_17_32AB(): pass

    label("Function_17_32AB")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_32AB end

    def Function_18_32C9(): pass

    label("Function_18_32C9")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_32C9 end

    def Function_19_32E7(): pass

    label("Function_19_32E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3302")
    Sound(540, 0, 50, 0)
    Jump("loc_3308")

    label("loc_3302")

    Sound(531, 0, 100, 0)

    label("loc_3308")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_32E7 end

    def Function_20_3320(): pass

    label("Function_20_3320")

    Sound(892, 0, 100, 0)
    OP_71(0x0, 0x1B9, 0x1C2, 0x1, 0x0)
    OP_74(0x0, 0x5)
    OP_79(0x0)
    OP_71(0x0, 0x1C3, 0x1D6, 0x1, 0x20)
    Return()

    # Function_20_3320 end

    def Function_21_3346(): pass

    label("Function_21_3346")

    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_71(0x0, 0xB, 0x32, 0x0, 0x20)
    Return()

    # Function_21_3346 end

    def Function_22_335C(): pass

    label("Function_22_335C")

    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_71(0x0, 0x3FC, 0x410, 0x0, 0x20)
    Return()

    # Function_22_335C end

    def Function_23_3372(): pass

    label("Function_23_3372")

    OP_71(0x0, 0x408, 0x410, 0x0, 0x0)
    OP_79(0x0)
    Sound(892, 0, 80, 0)
    OP_71(0x0, 0x411, 0x41A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xB, 0x32, 0x0, 0x20)
    Return()

    # Function_23_3372 end

    def Function_24_33A3(): pass

    label("Function_24_33A3")

    PlayEffect(0x2, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_24_33A3 end

    def Function_25_33EC(): pass

    label("Function_25_33EC")

    PlayEffect(0x2, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_25_33EC end

    def Function_26_3435(): pass

    label("Function_26_3435")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3451")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_26_3435")

    label("loc_3451")

    Return()

    # Function_26_3435 end

    def Function_27_3452(): pass

    label("Function_27_3452")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sleep(100)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0x10)
    Sleep(100)
    SetChrSubChip(0xFE, 0x11)
    Sleep(100)
    SetChrSubChip(0xFE, 0x12)
    Sleep(100)
    SetChrSubChip(0xFE, 0x13)
    Sleep(100)
    SetChrSubChip(0xFE, 0x14)
    Sleep(100)
    SetChrSubChip(0xFE, 0x15)
    Sleep(100)
    SetChrSubChip(0xFE, 0x16)
    Sleep(100)
    SetChrSubChip(0xFE, 0x17)
    Sleep(100)
    SetChrSubChip(0xFE, 0x18)
    Sleep(100)
    SetChrSubChip(0xFE, 0x19)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(100)
    Return()

    # Function_27_3452 end

    def Function_28_3533(): pass

    label("Function_28_3533")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    LoadChrToIndex("chr/ch03151.itc", 0x25)
    LoadChrToIndex("chr/ch03156.itc", 0x27)
    LoadChrToIndex("apl/ch51737.itc", 0x28)
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(3584)
    SoundLoad(3585)
    SoundLoad(2924)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35E1")
    Call(0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35AD")
    OP_CF(0x1, 0xF5, 0x5)
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_35AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35C7")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_35C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35E1")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_35E1")

    LoadEffect(0x0, "event/ev17011.eff")
    LoadEffect(0x1, "event/ev17091.eff")
    LoadEffect(0x2, "battle/cr004000.eff")
    LoadEffect(0x3, "battle/cr004001.eff")
    LoadEffect(0x4, "eff/cutin30.eff")
    LoadEffect(0x5, "battle/cr004100.eff")
    LoadEffect(0x6, "event/ev17008.eff")
    LoadEffect(0x7, "event/ev17005.eff")
    LoadEffect(0x8, "event/ev17092.eff")
    LoadEffect(0x9, "event/ev17080.eff")
    LoadEffect(0xA, "event/ev17009.eff")
    SetChrPos(0x101, 1120, 0, 28600, 0)
    SetChrPos(0x102, -1270, 0, 27570, 0)
    SetChrPos(0x103, 420, 0, 26870, 0)
    SetChrPos(0x104, -2540, 0, 28190, 0)
    SetChrPos(0xF4, 0, 0, 29540, 0)
    SetChrPos(0xF5, 2540, 0, 27990, 0)
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
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x0, 0x4)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 0, 0, 36000, 180)
    SetChrPos(0x9, 0, 0, 36000, 180)
    OP_78(0x0, 0x9)
    OP_93(0x9, 0xB4, 0x0)
    SetChrFlags(0x9, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    OP_87(0xA, 0x3, 0x0, "Null_vertic(1)", 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_68(0, 3500, 35890, 0)
    MoveCamera(24, 7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(8500, 3000)
    BeginChrThread(0x8, 0, 0, 30)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7543", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(833, 0, 60, 0)
    Sound(825, 2, 100, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x8, 1, 0, 29)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3584V#4S#40AOOOOOOOH...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3585V#4S#50AWAZYYY... DAMN\x01",
            "YOUuuuUU!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(-450, 1000, 30720, 0)
    MoveCamera(39, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14700, 0)
    Fade(500)
    CancelBlur(500)
    EndChrThread(0x8, 0x1)
    CancelBlur(500)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#12PKh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12PWhat the hell!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A29")

    ChrTalk(
        0x109,
        (
            "#10108F#12PH-He should've used up\x01",
            "all his physical strength\x01",
            "already, and yet...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AED")

    label("loc_3A29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A92")

    ChrTalk(
        0x106,
        (
            "#10708F#12PHe should've used up all\x01",
            "his physical strength\x01",
            "already, and yet...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AED")

    label("loc_3A92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AED")

    ChrTalk(
        0x10A,
        (
            "#00607F#12PHe should've used up all\x01",
            "his physical strength\x01",
            "already...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AED")

    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x105)
    Sleep(500)
    OP_68(340, 1000, 31940, 800)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    OP_9B(0x0, 0x105, 0x0, 0x21C, 0x320, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10406F#12PActually, I should've\x01",
            "done this... On that\x01",
            "rainy day.\x02\x03",
            "#10408FGoing all out... I was\x01",
            "too worried about your\x01",
            "safety.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(895, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x7, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    SetMessageWindowPos(50, 50, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "......!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10403F#12PHowever, this time, neither\x01",
            "as a Gralsritter, nor as a\x01",
            "Stigma owner...\x02\x03",
            "I will show you my greatest\x01",
            "attack as Wazy Hemisphere,\x01",
            "the Testaments' leader.\x02\x03",
            "#10402FJust like I did the first\x01",
            "time I met you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 2000, 31850, 0)
    MoveCamera(0, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13500, 2000)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40WHEH... GWAHAHA...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_6F(0x79)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4SVERY WELL! I'LL JUST\x01",
            "HAVE TO BRING YOU DOWN\x01",
            "WITH ME!!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EndChrThread(0x8, 0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x392, 0x3A2, 0x1, 0x0)
    Sound(532, 0, 100, 0)
    OP_68(0, 3400, 31000, 0)
    MoveCamera(352, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14750, 0)
    Fade(500)
    OP_68(70, 3000, 33350, 1200)
    MoveCamera(62, 39, 17, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(11430, 1200)
    OP_0D()
    OP_6F(0x79)
    OP_79(0x0)
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x105, 0, 0, 33)
    BeginChrThread(0x9, 1, 0, 32)
    BeginChrThread(0x9, 0, 0, 31)
    Sound(893, 0, 100, 0)
    Sound(3549, 255, 100, 0)
    OP_68(70, 1800, 33350, 400)
    MoveCamera(15, 7, 17, 400)
    OP_6E(600, 400)
    SetCameraDistance(11430, 400)
    OP_6F(0x79)
    Sleep(250)
    OP_68(-410, 800, 32090, 750)
    MoveCamera(314, 17, 0, 750)
    OP_6E(600, 750)
    SetCameraDistance(13430, 750)
    OP_6F(0x79)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetMessageWindowPos(280, 40, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#13A...Ah...\x07\x00\x02",
        )
    )

    SetChrChip(0x1, 0x105, 0x0, 0x0)
    StopEffect(0x5, 0x2)
    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        "#10411F#2924V#5P#40WGute nacht─\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    OP_68(50, 2000, 31400, 200)
    MoveCamera(317, 11, 0, 200)
    OP_6E(600, 200)
    SetCameraDistance(9380, 200)
    BeginChrThread(0x105, 0, 0, 35)
    Sleep(200)
    EndChrThread(0x105, 0x0)
    Call(0, 45)
    SetChrPos(0x8, 0, 0, 35000, 180)
    SetChrPos(0x9, 0, 0, 35000, 180)
    SetChrPos(0x105, 0, 2200, 33150, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x105, 0, 0, 36)
    OP_68(0, 2900, 33850, 0)
    MoveCamera(310, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(7500, 0)
    Fade(500)
    OP_0D()
    Sound(2390, 255, 100, 0)
    Sleep(2000)
    Sleep(500)
    Sound(3551, 255, 100, 0)
    SetMessageWindowPos(200, 20, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12A#5S#40AOOOOOH...!?\x07\x00\x02",
        )
    )

    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 0, 0, 37)
    Sleep(500)
    SetCameraDistance(10000, 1500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    CancelBlur(500)
    Sound(3093, 255, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 0, 0, 38)
    Sleep(500)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    OP_68(1000, 1500, 33500, 0)
    MoveCamera(239, 31, 1, 0)
    OP_6E(600, 0)
    SetCameraDistance(8630, 0)
    Fade(500)
    OP_71(0x0, 0x231, 0x244, 0x1, 0x0)
    OP_0D()
    WaitChrThread(0x105, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 39)
    Sound(2868, 255, 100, 0)

    ChrTalk(
        0x105,
        "#10407F#6P#5S#40W#12AOOOOH...!\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    StopSound(825, 1000, 100)
    BeginChrThread(0x105, 0, 0, 40)
    Sleep(400)
    OP_68(150, 1500, 34250, 700)
    MoveCamera(320, 16, 1, 700)
    OP_6E(600, 700)
    SetCameraDistance(14060, 700)
    Sleep(400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 41)
    Sleep(1700)
    CancelBlur(500)
    Sleep(100)
    StopEffect(0x3, 0x2)
    OP_6F(0x79)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 0)
    Sound(3544, 255, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Sleep(700)
    Sleep(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(350, 1300, 33250, 0)
    MoveCamera(7, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15380, 0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    ClearChrFlags(0xF4, 0x2)
    ClearChrFlags(0xF4, 0x1000)
    Fade(500)
    OP_0D()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(800)

    ChrTalk(
        0x103,
        "#00205F#6P#NAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_433A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4312")
    OP_FC(0x6)
    Jump("loc_4315")

    label("loc_4312")

    OP_FC(0xC)

    label("loc_4315")


    ChrTalk(
        0x109,
        "#10102F#13P#NHe did it...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DB")

    label("loc_433A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_438B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4364")
    OP_FC(0x6)
    Jump("loc_4367")

    label("loc_4364")

    OP_FC(0xC)

    label("loc_4367")


    ChrTalk(
        0x106,
        "#10702F#13P#NHe did it...\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DB")

    label("loc_438B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43DB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43B5")
    OP_FC(0x6)
    Jump("loc_43B8")

    label("loc_43B5")

    OP_FC(0xC)

    label("loc_43B8")


    ChrTalk(
        0x10A,
        "#00602F#13P#NDid he do it...?\x02",
    )

    CloseMessageWindow()

    label("loc_43DB")

    StopSound(832, 1000, 100)
    StopEffect(0x1, 0x2)
    Sleep(500)
    StopEffect(0x2, 0x2)
    Sleep(800)
    Fade(250)
    OP_0D()
    Sound(825, 2, 80, 0)
    Sound(843, 0, 100, 0)
    PlayEffect(0x1, 0x4, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-760, 1300, 37770, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(16500, 2000)
    Sleep(500)
    StopEffect(0x4, 0x2)
    Fade(1000)
    Sound(223, 0, 100, 0)
    Sound(817, 0, 100, 0)
    StopSound(825, 1000, 80)
    Call(0, 46)
    BeginChrThread(0x8, 0, 0, 47)
    SetChrPos(0x8, 0, -200, 38500, 225)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x4)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_44FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_44FE)
    OP_75(0x0, 0x1, 0x5DC)
    Sleep(1500)
    ClearMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002F#11PHe returned to his\x01",
            "original form!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#5PThank goodness...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(230, 1200, 35730, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13640, 0)
    SetChrSubChip(0x8, 0x8)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    Sleep(50)
    WaitChrThread(0x8, 0)

    def lambda_45F2():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_45F2)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_4612():
        OP_A6(0xFE, 0x0, 0x50, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4612)
    WaitChrThread(0x8, 2)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 43)
    WaitChrThread(0x8, 3)

    ChrTalk(
        0x8,
        (
            "#01602F#5P#50W...Heh... To think even\x01",
            "the finishing blow was\x01",
            "the same as that day...\x02\x03",
            "Pathetic... Really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#11P#30WWell, since you were demonized,\x01",
            "I guess it means that's your\x01",
            "limit.\x02\x03",
            "#10404FI think your sense to handle\x01",
            ""power" is the real deal...\x02\x03",
            "#10400FI think that if you had some\x01",
            "proper training under your belt,\x01",
            "you could become even stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01608F#5P#50WHmph... You don't have\x01",
            "to tell me... ...I'll\x01",
            "struggle...\x02\x03",
            "To force you down on\x01",
            "your hands and knees...\x01",
            "One day... Wazy...\x02\x03",
            "#01604FStill... Just this\x01",
            "once... ...I admit... my\x01",
            "defeat...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(500, 800, 33060, 0)
    MoveCamera(30, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19350, 0)
    Fade(500)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01601F#5P#50WAlso... Hey... You\x01",
            "guys...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#01603F#5P#50WI don't give a damn\x01",
            "about what will\x01",
            "happen... to you, but...\x02\x03",
            "I'm unable to stomach\x01",
            "that... ...that brat's\x01",
            "gloomy mug...\x02\x03",
            "#01601F#51WYou've got to... go all\x01",
            "out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PWald...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PHah... That goes without\x01",
            "sayin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#12P...Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01604F#5P#60W......Heh......\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 44)
    WaitChrThread(0x8, 3)
    EndChrThread(0x8, 0x1)
    SetCameraDistance(25350, 4500)
    MoveCamera(30, 20, 0, 4500)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 0, 50, 33620, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(3300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("m9060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_3533 end

    def Function_29_4B3E(): pass

    label("Function_29_4B3E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B7C")
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(2800)
    CancelBlur(500)
    Sleep(800)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(2750)
    CancelBlur(500)
    Sleep(800)
    Jump("Function_29_4B3E")

    label("loc_4B7C")

    Return()

    # Function_29_4B3E end

    def Function_30_4B7D(): pass

    label("Function_30_4B7D")

    PlayEffect(0x8, 0x5, 0x8, 0x1, 0, 50, 0, 0, 0, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_30_4B7D end

    def Function_31_4BB5(): pass

    label("Function_31_4BB5")


    def lambda_4BBA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4BBA)

    def lambda_4BCF():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BCF)
    Sleep(350)
    Sound(196, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0x96, 0xBB8, 0x2BC)
    Return()

    # Function_31_4BB5 end

    def Function_32_4C00(): pass

    label("Function_32_4C00")

    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    Return()

    # Function_32_4C00 end

    def Function_33_4C1C(): pass

    label("Function_33_4C1C")

    Sleep(200)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x80, 0x0)

    def lambda_4C47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C47)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x6A4, 0x0, 0xFFFFFDDA, 0xFA, 0x44C)
    Sleep(200)
    StopEffect(0x2, 0x2)
    PlayEffect(0x6, 0x2, 0x105, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 34)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xFFFFF95C, 0xFA, 0x64, 0x5DC, 0x3E8)
    ClearChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 3)
    Sound(326, 0, 70, 0)
    Return()

    # Function_33_4C1C end

    def Function_34_4CE8(): pass

    label("Function_34_4CE8")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(550)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_34_4CE8 end

    def Function_35_4D41(): pass

    label("Function_35_4D41")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(251, 0, 100, 0)
    Sound(238, 0, 50, 0)
    OP_9C(0xFE, 0x4E2, 0x4E2, 0xFA0, 0x514, 0x9C4)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_35_4D41 end

    def Function_36_4D8D(): pass

    label("Function_36_4D8D")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)

    label("loc_4DCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EAC")
    SetChrSubChip(0xFE, 0x1)
    Sound(534, 0, 50, 0)
    Sound(541, 0, 100, 0)
    Sleep(50)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    OP_71(0x0, 0x21D, 0x226, 0x0, 0x0)
    Sound(260, 0, 60, 0)
    Sound(501, 0, 40, 0)
    SetChrSubChip(0xFE, 0x1)
    Sound(541, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    OP_71(0x0, 0x21D, 0x226, 0x0, 0x0)
    Jump("loc_4DCA")

    label("loc_4EAC")

    SetChrSubChip(0xFE, 0x5)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Return()

    # Function_36_4D8D end

    def Function_37_4ECB(): pass

    label("Function_37_4ECB")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(561, 0, 100, 0)
    Sound(881, 0, 80, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(1200)
    Sound(265, 0, 80, 0)
    Sound(501, 0, 50, 0)
    Sound(833, 0, 100, 0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x21D, 0x21E, 0x0, 0x0)
    OP_82(0x0, 0x96, 0xBB8, 0x2BC)

    def lambda_4FB1():
        OP_A6(0xFE, 0x96, 0x96, 0x96, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FB1)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    OP_71(0x0, 0x21E, 0x226, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(150)
    Return()

    # Function_37_4ECB end

    def Function_38_4FE7(): pass

    label("Function_38_4FE7")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x2BC, 0x0, 0xFFFFFE0C, 0x2EE, 0x3E8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x8)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Return()

    # Function_38_4FE7 end

    def Function_39_5040(): pass

    label("Function_39_5040")

    Sleep(1000)
    SetChrSubChip(0x105, 0x9)
    Fade(250)
    OP_0D()
    Return()

    # Function_39_5040 end

    def Function_40_504E(): pass

    label("Function_40_504E")

    SetChrSubChip(0xFE, 0xA)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5062():
        OP_9C(0xFE, 0x0, 0x708, 0x0, 0x73A, 0x514)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5062)
    Sound(321, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    EndChrThread(0xFE, 0x1)
    OP_82(0x96, 0x96, 0xBB8, 0x3E8)
    Sound(815, 0, 100, 0)
    Sound(666, 0, 100, 0)
    Sleep(400)

    def lambda_50E3():
        OP_9C(0xFE, 0x0, 0xFFFFFB1E, 0x0, 0xFA, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50E3)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    Return()

    # Function_40_504E end

    def Function_41_510E(): pass

    label("Function_41_510E")

    BeginChrThread(0xFE, 3, 0, 42)

    def lambda_5119():
        OP_9C(0xFE, 0x0, 0x0, 0x9C4, 0xDAC, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5119)
    OP_9C(0xFE, 0x0, 0x258, 0x3E8, 0x9C4, 0x12C)
    OP_82(0x96, 0x96, 0xBB8, 0x3E8)
    Sound(833, 0, 100, 0)
    Sound(627, 0, 100, 0)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_41_510E end

    def Function_42_518E(): pass

    label("Function_42_518E")

    OP_71(0x0, 0x244, 0x231, 0x1, 0x0)
    OP_D5(0xFE, 0xFFFEB3F8, 0x2BF20, 0x0, 0x9C4)
    Return()

    # Function_42_518E end

    def Function_43_51AE(): pass

    label("Function_43_51AE")

    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(300)
    Return()

    # Function_43_51AE end

    def Function_44_51C3(): pass

    label("Function_44_51C3")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    Sound(862, 0, 20, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(100)
    Sound(811, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(300)
    Return()

    # Function_44_51C3 end

    def Function_45_51EB(): pass

    label("Function_45_51EB")

    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Return()

    # Function_45_51EB end

    def Function_46_5278(): pass

    label("Function_46_5278")

    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x1, 0x1)
    Return()

    # Function_46_5278 end

    def Function_47_5305(): pass

    label("Function_47_5305")

    StopSound(154, 1000, 50)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Sleep(200)
    Return()

    # Function_47_5305 end

    def Function_48_53AD(): pass

    label("Function_48_53AD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53CE")
    Call(0, 5)

    label("loc_53CE")

    LoadChrToIndex("chr/ch03156.itc", 0x1F)
    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, 120, 0, 30600, 354)
    SetChrPos(0x102, -2270, 0, 29570, 21)
    SetChrPos(0x103, -580, 0, 28870, 2)
    SetChrPos(0x104, -3540, 0, 30190, 35)
    SetChrPos(0xF4, -300, 0, 32650, 0)
    SetChrPos(0xF5, 1540, 0, 29990, 338)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, -200, 38500, 225)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    OP_68(0, 50, 45000, 0)
    MoveCamera(39, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 45000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-1720, 1100, 32000, 0)
    MoveCamera(39, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13330, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        "#10406F#11P#30WPhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#11P...Nice work, Wazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PGood work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11P#30WHehe... I guess I'm\x01",
            "really tired.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(811, 0, 50, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5771():
        OP_9B(0x0, 0xFE, 0x0, 0x190, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5771)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00005F#11PH-Hey!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57EF")

    ChrTalk(
        0x109,
        "#10111F#11PWazy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PA-Are you all right!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5822")

    label("loc_57EF")


    ChrTalk(
        0x102,
        "#00105F#12PWazy...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12PYou ok!?\x02",
    )

    CloseMessageWindow()

    label("loc_5822")


    ChrTalk(
        0x105,
        (
            "#10406F#11P#40W*pant*... When I use the\x01",
            "Stigma power... there\x01",
            "are side effects...\x02\x03",
            "#10408FCould I really have\x01",
            "gone... a bit too\x01",
            "overboard...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5908")

    ChrTalk(
        0x109,
        (
            "#10106F#11PHonestly... You keep\x01",
            "doing reckless things...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_599F")

    label("loc_5908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5948")

    ChrTalk(
        0x10A,
        (
            "#00606F#11PHmph, such\x01",
            "recklessness...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_599F")

    label("loc_5948")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_599F")

    ChrTalk(
        0x106,
        (
            "#10706F#11P...I can't blame you.\x01",
            "Against such a giant\x01",
            "opponent...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_599F")


    ChrTalk(
        0x101,
        "#00013F#11P...Are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11P#30WWell, somehow or\x01",
            "other...\x02\x03",
            "#10400F─Upsy-daisy.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_68(-1720, 1100, 32000, 800)
    MoveCamera(44, 12, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(13330, 800)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)
    TurnDirection(0x105, 0x101, 400)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10403F#5PWith this, this\x01",
            "Territory has probably\x01",
            "been released...\x02\x03",
            "#10401FWe'll come get Wald\x01",
            "later, so let's return\x01",
            "to the gate for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PUnderstood... Let's try\x01",
            "heading back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PC'mon, I'll lend you my\x01",
            "shoulder.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 0, 0, 49)
    SetCameraDistance(12600, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    EndChrThread(0x104, 0x0)
    SetChrPos(0x0, 0, 0, 32619, 0)
    SetChrSubChip(0x8, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A7, 7)
    OP_29(0xB2, 0x1, 0x3)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7354", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_48_53AD end

    def Function_49_5BCB(): pass

    label("Function_49_5BCB")

    TurnDirection(0xFE, 0x105, 500)
    OP_9B(0x0, 0xFE, 0x161, 0x9C4, 0x5DC, 0x0)
    Return()

    # Function_49_5BCB end

    def Function_50_5BE2(): pass

    label("Function_50_5BE2")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x1000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_50_5BE2 end

    SaveToFile()

Try(main)
