from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3600.bin",                # FileName
        "e3600",                    # MapName
        "e3600",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3600",                  # 0
        "Ilya",                   # 1
        "Rixia",                  # 2
        "Sully",                  # 3
        "Eugene",                 # 4
        "Theodore",               # 5
        "Nikol",                  # 6
        "Pliｳ",                  # 7
        "Celine",                 # 8
        "Bloody Shirley",         # 9
        "Jaeger",                 # 10
        "Jaeger",                 # 11
        "Jaeger",                 # 12
        "Jaeger",                 # 13
        "Spectator",              # 14
        "Spectator",              # 15
        "Spectator",              # 16
        "Spectator",              # 17
        "Spectator",              # 18
        "Spectator",              # 19
        "Spectator",              # 20
        "Spectator",              # 21
        "Spectator",              # 22
        "Spectator",              # 23
        "Spectator",              # 24
        "Spectator",              # 25
        "Spectator",              # 26
        "Spectator",              # 27
        "Spectator",              # 28
        "Spectator",              # 29
        "Spectator",              # 30
        "Spectator",              # 31
        "Spectator",              # 32
        "Spectator",              # 33
        "降魔刀",                 # 34
        "SE制御",                 # 35
    ))

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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1360, 0)                                       # 0

    ScpFunction((
        "Function_0_550",          # 00, 0
        "Function_1_574",          # 01, 1
        "Function_2_575",          # 02, 2
        "Function_3_2C9E",         # 03, 3
        "Function_4_2CE1",         # 04, 4
        "Function_5_2CFA",         # 05, 5
        "Function_6_2D13",         # 06, 6
        "Function_7_2D43",         # 07, 7
        "Function_8_2D73",         # 08, 8
        "Function_9_2DA3",         # 09, 9
        "Function_10_2DE7",        # 0A, 10
        "Function_11_2E03",        # 0B, 11
        "Function_12_2E33",        # 0C, 12
        "Function_13_2E4F",        # 0D, 13
        "Function_14_2E7F",        # 0E, 14
        "Function_15_2EA8",        # 0F, 15
        "Function_16_2ED8",        # 10, 16
        "Function_17_2F01",        # 11, 17
        "Function_18_2F31",        # 12, 18
        "Function_19_2F5A",        # 13, 19
        "Function_20_2FAA",        # 14, 20
        "Function_21_2FF0",        # 15, 21
        "Function_22_3036",        # 16, 22
        "Function_23_307C",        # 17, 23
        "Function_24_30C2",        # 18, 24
        "Function_25_3112",        # 19, 25
        "Function_26_3162",        # 1A, 26
        "Function_27_31B2",        # 1B, 27
        "Function_28_31D3",        # 1C, 28
        "Function_29_3217",        # 1D, 29
        "Function_30_325B",        # 1E, 30
        "Function_31_329F",        # 1F, 31
        "Function_32_32E3",        # 20, 32
        "Function_33_3327",        # 21, 33
        "Function_34_336B",        # 22, 34
        "Function_35_33AF",        # 23, 35
        "Function_36_33F3",        # 24, 36
        "Function_37_3447",        # 25, 37
        "Function_38_345F",        # 26, 38
        "Function_39_3641",        # 27, 39
        "Function_40_3C2E",        # 28, 40
        "Function_41_488F",        # 29, 41
        "Function_42_48B3",        # 2A, 42
        "Function_43_48D7",        # 2B, 43
        "Function_44_48EC",        # 2C, 44
        "Function_45_48FA",        # 2D, 45
        "Function_46_4919",        # 2E, 46
        "Function_47_4938",        # 2F, 47
        "Function_48_4983",        # 30, 48
        "Function_49_49C9",        # 31, 49
        "Function_50_49DC",        # 32, 50
        "Function_51_49F8",        # 33, 51
        "Function_52_4C6A",        # 34, 52
        "Function_53_4DE8",        # 35, 53
        "Function_54_5111",        # 36, 54
        "Function_55_5142",        # 37, 55
        "Function_56_578C",        # 38, 56
        "Function_57_5D0B",        # 39, 57
    ))


    def Function_0_550(): pass

    label("Function_0_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_564")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_573")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_573")
    ClearScenarioFlags(0x22, 1)
    Event(0, 57)

    label("loc_573")

    Return()

    # Function_0_550 end

    def Function_1_574(): pass

    label("Function_1_574")

    Return()

    # Function_1_574 end

    def Function_2_575(): pass

    label("Function_2_575")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32300.itc", 0x23)
    LoadChrToIndex("chr/ch32400.itc", 0x24)
    LoadChrToIndex("chr/ch33000.itc", 0x25)
    LoadChrToIndex("chr/ch33100.itc", 0x26)
    LoadChrToIndex("chr/ch33300.itc", 0x27)
    LoadChrToIndex("chr/ch26900.itc", 0x28)
    LoadChrToIndex("chr/ch28100.itc", 0x29)
    LoadChrToIndex("apl/ch50250.itc", 0x2D)
    LoadChrToIndex("apl/ch50251.itc", 0x2E)
    LoadChrToIndex("apl/ch50252.itc", 0x2F)
    LoadChrToIndex("apl/ch50253.itc", 0x30)
    LoadChrToIndex("apl/ch50254.itc", 0x31)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis410.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06200.itp")
    LoadEffect(0x0, "event/ev15001.eff")
    LoadEffect(0x1, "event/ev15002.eff")
    LoadEffect(0x2, "event/ev15003.eff")
    LoadEffect(0x3, "event/ev15009.eff")
    SoundLoad(818)
    SoundLoad(819)
    SoundLoad(3250)
    SoundLoad(3251)
    SoundLoad(3252)
    SoundLoad(3253)
    SoundLoad(3957)
    SoundLoad(3958)
    SoundLoad(3959)
    SoundLoad(3960)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    OP_71(0x1, 0x0, 0x0, 0x1, 0x0)
    OP_7D(0xA0, 0xA0, 0xD2, 0x0, 0x0)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 3500, 1800, 27700, 225)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 1250, 25500, 225)
    BeginChrThread(0x0, 0, 0, 38)
    OP_68(0, 2900, 24750, 0)
    MoveCamera(5, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30500, 0)
    OP_68(0, 2900, 24750, 8000)
    MoveCamera(-5, 10, 0, 8000)
    OP_6E(700, 8000)
    SetCameraDistance(30500, 8000)
    VolumeBGM(0x64, 0x3E8)
    BeginChrThread(0x2A, 1, 0, 49)
    FadeToBright(1000, 0)
    Sleep(7500)
    OP_68(0, 4900, 25220, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16000, 0)
    OP_68(0, 2900, 25220, 8000)
    MoveCamera(5, 15, 1, 8000)
    SetCameraDistance(15000, 8000)
    BeginChrThread(0x2A, 1, 0, 50)
    Fade(500)
    WaitChrThread(0x0, 0)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x8, 0xFF)
    OP_49()
    LoadChrToIndex("chr/ch36600.itc", 0x1E)
    LoadChrToIndex("chr/ch36700.itc", 0x1F)
    LoadChrToIndex("chr/ch36900.itc", 0x20)
    LoadChrToIndex("chr/ch37000.itc", 0x21)
    LoadChrToIndex("chr/ch36800.itc", 0x22)
    LoadChrToIndex("chr/ch41951.itc", 0x4B)
    LoadChrToIndex("chr/ch41952.itc", 0x4C)
    LoadChrToIndex("apl/ch51505.itc", 0x4D)
    LoadChrToIndex("chr/ch03450.itc", 0x46)
    LoadChrToIndex("chr/ch03452.itc", 0x47)
    LoadChrToIndex("chr/ch03456.itc", 0x48)
    LoadChrToIndex("chr/ch0345F.itc", 0x49)
    LoadChrToIndex("apl/ch51506.itc", 0x4A)
    LoadChrToIndex("chr/ch09800.itc", 0x41)
    LoadChrToIndex("apl/ch51503.itc", 0x42)
    LoadChrToIndex("apl/ch51507.itc", 0x43)
    LoadChrToIndex("apl/ch51504.itc", 0x32)
    LoadChrToIndex("apl/ch51501.itc", 0x3C)
    LoadChrToIndex("apl/ch51502.itc", 0x3D)
    LoadChrToIndex("chr/ch14100.itc", 0x3E)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev15021.eff")
    LoadEffect(0x2, "event/ev15000.eff")
    LoadEffect(0x3, "event/ev15010.eff")
    LoadEffect(0x4, "event/ev15011.eff")
    LoadEffect(0x5, "event/ev15020.eff")
    LoadEffect(0x6, "battle/ms00001.eff")
    SoundLoad(870)
    SoundLoad(875)
    SoundLoad(877)
    SoundLoad(566)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(868)
    SoundLoad(926)
    SetChrChipByIndex(0x9, 0x41)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x9, -62260, 0, 4180, 135)
    SetChrPos(0xD, -63950, 0, 3170, 90)
    SetChrPos(0xE, -63620, 0, 4410, 135)
    SetChrPos(0xF, -63000, 0, 2460, 90)
    SetChrPos(0xB, -64580, 0, 1750, 90)
    SetChrPos(0xC, -65410, 0, 2420, 90)
    OP_68(-63820, 1200, 3260, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(16000, 1500)
    VolumeBGM(0x46, 0x3E8)
    Sound(818, 0, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xD,
        (
            "#5PAmazing... Sully really\x01",
            "did her best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PHaha, she trains her\x01",
            "heart out every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PH-Hmph... Not too bad, I\x01",
            "suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6PHaha, but that new scene\x01",
            "alone changes\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PYeah, Ilya and the\x01",
            "director wouldn't let\x01",
            "that one go.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#30W...Yes...\x02\x03",
            "(If Sully's here, then even if I'm\x01",
            "not...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C5F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C5F)
    WaitChrThread(0x9, 2)
    Sleep(150)

    ChrTalk(
        0x9,
        "#06205F#5P#30WHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_CEE():
        TurnDirection(0xE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_CEE)
    Sleep(50)

    def lambda_CFE():
        TurnDirection(0xF, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_CFE)
    Sleep(50)

    def lambda_D0E():
        TurnDirection(0xB, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_D0E)
    Sleep(50)

    def lambda_D1E():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_D1E)
    Sleep(50)

    def lambda_D2E():
        TurnDirection(0xD, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D2E)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0xE,
        "#5PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6PDid you see something\x01",
            "strange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6208F#5P#40WT-This presence is...\x02\x03",
            "#6203F#40WFive... No, ten of\x01",
            "them... Why now?\x02\x03",
            "#6201F#20WIt can't be!\x02",
        )
    )

    CloseMessageWindow()
    Sound(872, 0, 50, 0)
    Sleep(500)
    Sound(870, 2, 50, 0)
    Sleep(500)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_E97():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_E97)
    Sleep(50)

    def lambda_EA7():
        OP_93(0xE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_EA7)
    Sleep(50)

    def lambda_EB7():
        OP_93(0xF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_EB7)
    Sleep(50)

    def lambda_EC7():
        OP_93(0xB, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_EC7)
    Sleep(50)

    def lambda_ED7():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_ED7)
    Sleep(50)

    def lambda_EE7():
        OP_93(0xD, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_EE7)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    ChrTalk(
        0xF,
        "#5PW-What's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "A-Above us!?\x02",
    )

    CloseMessageWindow()
    OP_68(-62820, 1200, 3260, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x10, 0x46)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 13500, 31350, 180)
    OP_68(0, 14500, 31350, 0)
    MoveCamera(15, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 14500, 31350, 2000)
    MoveCamera(5, 15, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(16000, 2000)
    VolumeBGM(0x64, 0x3E8)
    StopSound(870, 1000, 40)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x10, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x10,
        (
            "Haha. Thank goodness I made it in\x01",
            "time.\x02\x03",
            "It's a waste to spoil that special\x01",
            "additional scene, but...\x02\x03",
            "Everyone'll be so excited, so I\x01",
            "guess it doesn't matter.\x02",
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
    OP_68(0, 14750, 26900, 500)
    MoveCamera(330, 20, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(15500, 500)
    OP_F0(0x0, 0xB)
    SetChrChipByIndex(0x10, 0x47)
    SetChrSubChip(0x10, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0x10, 0x0, 0x35B6, 0x6914, 0x5DC, 0x1B58)
    BeginChrThread(0x10, 3, 0, 4)
    Sound(872, 0, 100, 0)
    Sleep(500)
    Sound(870, 2, 90, 0)
    EndChrThread(0x10, 0x3)
    BeginChrThread(0x10, 3, 0, 5)
    OP_87(0x2, 0x0, 0x1, "CA00", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sound(875, 2, 90, 0)
    Sound(566, 0, 70, 0)
    Sound(358, 0, 70, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x10,
        "#04612F#3957V#11P#5S#20A#30WAhahahaha, fall!!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6B(0xFF)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    OP_87(0x6, 0x1, 0x1, "CA00", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_71(0x1, 0x2C, 0x50, 0x1, 0x8)
    Sound(873, 0, 100, 0)
    StopSound(870, 500, 80)
    StopSound(875, 500, 80)
    EndChrThread(0x10, 0x3)
    StopEffect(0x0, 0x0)
    SetChrChipByIndex(0x10, 0x49)
    SetChrSubChip(0x10, 0x2)
    Sound(834, 0, 100, 0)
    Sound(844, 0, 100, 0)
    OP_9D(0x10, 0x834, 0x34BC, 0x78B4, 0x7D0, 0x1B58)
    SetChrSubChip(0x10, 0x0)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x2)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    SetChrPos(0x8, 1800, 1250, 28100, 225)
    SetChrPos(0xA, 0, 1250, 25450, 180)
    SetChrPos(0x9, -10000, 1250, 24750, 90)
    SetChrPos(0xB, -12500, 1250, 24750, 90)
    SetChrPos(0xC, -14000, 1250, 24750, 90)
    SetChrPos(0xD, -15500, 1250, 24750, 90)
    SetChrPos(0xF, -17000, 1250, 24750, 90)
    SetChrPos(0xE, -18500, 1250, 24750, 90)
    OP_68(0, 3250, 24900, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18000, 500)
    OP_71(0x1, 0x0, 0x0, 0x1, 0x0)
    OP_0D()
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        "#12211F#7AHuh?\x02",
    )

    Sleep(600)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#06107F#4S#9AGet down!!\x02",
    )

    Sleep(1500)
    SetChrChipByIndex(0x8, 0x2E)

    def lambda_13F5():
        OP_9A(0xFE, 0xA, 0x1F4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13F5)
    Sleep(200)
    Sound(811, 0, 100, 0)
    Sound(862, 0, 100, 0)
    Fade(100)
    OP_71(0x1, 0x2C, 0x2C, 0x0, 0x0)
    OP_68(0, 11000, 25450, 0)
    MoveCamera(0, -30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_F0(0x0, 0xA)
    OP_68(0, 3250, 24900, 500)
    MoveCamera(0, 15, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x2C, 0x36, 0x1, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    Sleep(400)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x31)
    SetChrSubChip(0x8, 0x1)
    OP_93(0x8, 0xB4, 0x0)
    ClearChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x1)

    def lambda_14D7():
        OP_96(0xFE, 0xFFFFF1BE, 0x4E2, 0x5302, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14D7)

    def lambda_14F1():
        OP_96(0xFE, 0xFFFFFAEC, 0x4E2, 0x5B04, 0x251C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14F1)
    OP_68(0, 2250, 24900, 500)
    MoveCamera(0, 30, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(22000, 500)
    OP_74(0x1, 0x1E)
    OP_79(0x1)
    OP_71(0x1, 0x37, 0x50, 0x1, 0x8)
    Sound(876, 0, 100, 0)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 40, 0)
    Sound(833, 0, 60, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 1250, 25450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_71(0x5, 0x2, 0x1E, 0x0, 0x8)
    ClearMapObjFlags(0x6, 0x4)
    OP_71(0x6, 0x0, 0xC, 0x0, 0x8)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0x8, 0x20)
    OP_6F(0x79)
    StopBGM(0x3E8)
    Sleep(2000)
    PlayEffect(0x4, 0xFF, 0x8, 0x0, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(0, 2250, 24900, 20000)
    MoveCamera(0, 35, -5, 20000)
    OP_6E(600, 20000)
    SetCameraDistance(22000, 20000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x2A, 1, 0, 48)
    Sleep(1000)
    Sound(878, 0, 80, 0)

    ChrTalk(
        0x15,
        "#3PWhaaa!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#4PI-Ilya was...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x17,
        "#4SIlya's trapped!?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sound(802, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3D)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        "#12211F#50WY-Yeah...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#06214F#3250V#4SIlya!!!\x02",
    )

    CloseMessageWindow()
    OP_24(0xCB2)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-2550, 2250, 21750, 0)
    MoveCamera(345, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    MoveCamera(8, 26, 0, 3500)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xB, 3, 0, 9)
    BeginChrThread(0xC, 3, 0, 11)
    BeginChrThread(0xD, 3, 0, 13)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0xE, 3, 0, 17)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)

    ChrTalk(
        0xA,
        "#12210F#6PR-Rixia!\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)

    def lambda_17F3():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_17F3)

    def lambda_180C():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_180C)
    Sound(879, 0, 100, 0)
    OP_25(0x36D, 0x46)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x51, 0x67, 0x1, 0x8)
    OP_79(0x1)
    Sound(812, 0, 100, 0)

    def lambda_1848():

        label("loc_1848")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1848")

    QueueWorkItem2(0xD, 2, lambda_1848)

    def lambda_185A():

        label("loc_185A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_185A")

    QueueWorkItem2(0xF, 2, lambda_185A)

    def lambda_186C():

        label("loc_186C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_186C")

    QueueWorkItem2(0xE, 2, lambda_186C)

    def lambda_187E():
        OP_96(0xFE, 0xFFFFF448, 0x4E2, 0x5460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_187E)
    SetChrFlags(0x8, 0x20)
    TurnDirection(0x8, 0x9, 0)

    def lambda_18A4():
        OP_96(0xFE, 0xFFFFF736, 0x4E2, 0x5686, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18A4)
    WaitChrThread(0x8, 1)
    ClearChrFlags(0x8, 0x20)
    WaitChrThread(0x9, 1)
    BeginChrThread(0x9, 3, 0, 7)
    WaitChrThread(0x9, 3)
    Sound(880, 0, 100, 0)
    OP_25(0x36D, 0x28)
    OP_71(0x1, 0x68, 0x72, 0x1, 0x8)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x42)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_79(0x1)
    EndChrThread(0xB, 0x3)

    def lambda_191A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_191A)
    Sleep(100)
    EndChrThread(0xC, 0x3)

    def lambda_192E():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_192E)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xE, 0x2)
    OP_0D()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        "#06212F#3251V#11PIlya!? No, Ilya!\x02",
    )

    CloseMessageWindow()
    OP_24(0xCB3)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#5P...How could this\x01",
            "happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PW-Why did you...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-2250, 2150, 22250, 20000)
    MoveCamera(6, 31, 0, 20000)
    OP_6E(500, 20000)
    SetCameraDistance(15500, 20000)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x8, 0x2)
    OP_0D()

    ChrTalk(
        0x8,
        "#06110F#5P#80W#2S...Ugh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#06212F#11PIlya!? Are you alright,\x01",
            "Ilya!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06111F#5P#80W#2S...What about...\x01",
            "Sully...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x38)
    OP_9A(0xA, 0x8, 0x2EE, 0x7D0, 0x0)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3D)
    SetChrSubChip(0xA, 0x1)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#12210F#6PI'm fine!\x02\x03",
            "It's because you saved\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x8, 0x4)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#06110F#5P#80W#2S...Oh... Good...\x02\x03",
            "#2S#80W...Ri...xia... The\x01",
            "next... act... Only...\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(300)
    Sound(812, 0, 100, 0)
    SetCameraDistance(15000, 300)
    SetChrSubChip(0x8, 0x5)
    OP_0D()
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#06214F#11P#4SIlya!?... Ilya!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12210F#6PUwaaaah!!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        "#11PTheo, carry her!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        "#5PUnderstood!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 10)
    Sleep(300)
    BeginChrThread(0xC, 3, 0, 12)
    Sound(812, 0, 100, 0)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Sleep(300)
    ClearChrFlags(0x10, 0x80)

    NpcTalk(
        0x10,
        "Shirley's Voice",
        (
            "Oh, was the show that\x01",
            "important?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x10, 0x49)
    SetChrSubChip(0x10, 0x1)
    SetChrPos(0x10, 3900, 13500, 29750, 225)
    SetChrPos(0x9, -1800, 1250, 19850, 0)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x41)
    SetChrSubChip(0x9, 0x0)
    OP_68(3200, 8700, 30850, 0)
    MoveCamera(30, -15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 6300, 30600, 2000)
    MoveCamera(0, 15, 0, 2000)
    SetCameraDistance(16500, 2000)
    SetChrChip(0x0, 0x10, 0x1E, 0xC8)
    OP_9D(0x10, 0x9F6, 0x1DB0, 0x7788, 0x3E8, 0x1B58)
    Sound(809, 0, 50, 0)
    OP_9D(0x10, 0x0, 0x14B4, 0x7788, 0x3E8, 0x1B58)
    SetChrSubChip(0x10, 0x0)
    Sound(326, 0, 30, 0)
    SetChrChipByIndex(0x10, 0x46)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0xB4, 0x1F4)
    SetChrChip(0x1, 0x10, 0x0, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x2710)
    SetCameraDistance(15500, 20000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)

    ChrTalk(
        0x10,
        (
            "#04609F#11PAha! Ilya sure is\x01",
            "amazing!\x02\x03",
            "#04602FI totally get why you\x01",
            "fell for her, Rixia♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06211F#40WBloody Shirley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "A-A girl...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "W-Who's that!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 80, 0)
    SetChrChipByIndex(0x10, 0x48)
    OP_A1(0x10, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0x10, 3, 0, 19)
    Sleep(500)
    StopSound(865, 300, 100)
    StopSound(861, 300, 50)
    EndChrThread(0x10, 0x3)
    OP_0D()
    Sleep(300)
    Sound(878, 0, 80, 0)
    SetMessageWindowPos(-1, 200, -1, -1)

    AnonymousTalk(
        0x15,
        "EEEEEEK!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 200, -1, -1)

    AnonymousTalk(
        0x16,
        "A g-gun!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 200, -1, -1)

    AnonymousTalk(
        0x1B,
        "She's got a gun!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    Sound(937, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x4B)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x4B)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x4B)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x4B)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x11, 600, 2700, -4900, 0)
    SetChrPos(0x12, -600, 2700, -5400, 0)
    SetChrPos(0x13, 600, 2700, -6400, 0)
    SetChrPos(0x14, -600, 2700, -6900, 0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x4)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 3200, 2250, 2700, 350)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 2000, 1800, 4800, 350)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 2950, 1800, 5000, 350)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 3950, 1800, 5150, 350)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 4200, 1350, 7350, 350)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 5250, 1350, 7500, 350)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 2100, 900, 9150, 350)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 2850, 900, 9300, 350)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 3800, 900, 9450, 350)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 4800, 900, 9650, 350)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -2100, 2250, 2600, 10)
    SetChrChipByIndex(0x20, 0x23)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -3250, 2250, 2800, 10)
    SetChrChipByIndex(0x21, 0x27)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -3100, 1800, 4950, 10)
    SetChrChipByIndex(0x22, 0x25)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -4050, 1800, 5100, 10)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -2150, 1350, 6800, 10)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -3300, 1350, 7000, 10)
    SetChrChipByIndex(0x25, 0x26)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, -4300, 1350, 7150, 10)
    SetChrChipByIndex(0x26, 0x25)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -1950, 900, 9000, 10)
    SetChrChipByIndex(0x27, 0x26)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, -2950, 900, 9150, 10)
    SetChrChipByIndex(0x28, 0x24)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, -3900, 900, 9300, 10)
    OP_68(0, 4000, -2800, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 700, 15500, 5000)
    MoveCamera(0, 17, -5, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(23500, 5000)

    def lambda_238A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_238A)

    def lambda_239B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_239B)

    def lambda_23AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_23AC)

    def lambda_23BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_23BD)
    BeginChrThread(0x11, 1, 0, 20)
    BeginChrThread(0x12, 1, 0, 21)
    BeginChrThread(0x13, 1, 0, 22)
    BeginChrThread(0x14, 1, 0, 23)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    SetChrChipByIndex(0x11, 0x4D)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x12, 0x4D)
    SetChrSubChip(0x12, 0x4)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x13, 0x4D)
    SetChrSubChip(0x13, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x14, 0x4D)
    SetChrSubChip(0x14, 0x2)
    SetChrFlags(0x14, 0x2)
    OP_0D()
    Sound(865, 2, 100, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0x11, 3, 0, 24)
    BeginChrThread(0x12, 3, 0, 25)
    BeginChrThread(0x13, 3, 0, 26)
    BeginChrThread(0x14, 3, 0, 26)
    Sleep(500)
    StopSound(865, 300, 100)
    StopSound(861, 300, 50)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x3)
    OP_0D()
    Sound(878, 0, 100, 0)
    Sound(916, 0, 80, 0)

    ChrTalk(
        0x15,
        "Eeeeek!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "S-Save me! Aidioooos!!\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 2, 30, 0)
    Sound(937, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    BeginChrThread(0x1F, 1, 0, 29)
    Sleep(50)
    BeginChrThread(0x16, 1, 0, 30)
    Sleep(50)
    BeginChrThread(0x23, 1, 0, 33)
    Sleep(50)
    BeginChrThread(0x1B, 1, 0, 34)
    Sleep(50)
    BeginChrThread(0x26, 1, 0, 35)
    Sleep(100)
    BeginChrThread(0x15, 1, 0, 28)
    Sleep(50)
    BeginChrThread(0x20, 1, 0, 29)
    Sleep(50)
    BeginChrThread(0x17, 1, 0, 30)
    Sleep(50)
    BeginChrThread(0x21, 1, 0, 31)
    Sleep(50)
    BeginChrThread(0x24, 1, 0, 33)
    Sleep(50)
    BeginChrThread(0x1C, 1, 0, 34)
    Sleep(50)
    BeginChrThread(0x27, 1, 0, 35)
    Sleep(100)
    BeginChrThread(0x18, 1, 0, 30)
    Sleep(50)
    BeginChrThread(0x22, 1, 0, 31)
    Sleep(50)
    BeginChrThread(0x19, 1, 0, 32)
    Sleep(50)
    BeginChrThread(0x25, 1, 0, 33)
    Sleep(50)
    BeginChrThread(0x1D, 1, 0, 34)
    Sleep(50)
    BeginChrThread(0x28, 1, 0, 35)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x26, 0x1)
    EndChrThread(0x27, 0x1)
    EndChrThread(0x28, 0x1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_25(0x364, 0x32)
    OP_82(0x32, 0x32, 0xBB8, 0x0)
    Fade(500)
    SetMapObjFlags(0x2, 0x4)
    SetChrPos(0xA, -3650, 1250, 21050, 135)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x29, 0x4A)
    SetChrSubChip(0x29, 0x8)
    SetChrFlags(0x29, 0x8000)
    SetChrFlags(0x29, 0x2)
    SetChrFlags(0x29, 0x20)
    ClearChrFlags(0x29, 0x1)
    SetChrPos(0x29, 0, 5500, 30600, 0)
    OP_93(0x9, 0x0, 0x0)
    TurnDirection(0xB, 0x9, 0)
    TurnDirection(0xC, 0x9, 0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x42)
    SetChrSubChip(0x9, 0x3)
    OP_68(-1850, 2250, 20000, 0)
    MoveCamera(335, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(315, 30, 0, 6000)
    SetCameraDistance(15000, 6000)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -8200, 0, 18930, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -3880, 7600, 30690, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 2310, 1250, 22120, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_0D()
    TurnDirection(0xB, 0x8, 500)
    Sleep(50)
    TurnDirection(0xC, 0x8, 500)
    BeginChrThread(0xE, 1, 0, 18)
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0xD, 1, 0, 14)
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 1, 0, 36)
    BeginChrThread(0xC, 1, 0, 36)
    BeginChrThread(0xB, 1, 0, 36)
    Sleep(2000)

    def lambda_2839():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2839)
    WaitChrThread(0x9, 2)
    Sleep(800)

    def lambda_2859():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2859)
    WaitChrThread(0x9, 2)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        "#06213F#3252V#6P#50W...You... All of you...\x02",
    )

    CloseMessageWindow()
    OP_24(0xCB4)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10,
        (
            "#04612F#3958V#12P#N#30WAhaha, yeah, yeah! You\x01",
            "saw that, huh!?\x02\x03",
            "#04611F#3959VUnbridled "strength"!\x02\x03",
            "#3960VThe true power of Rixia\x01",
            "Mao, without wasting\x01",
            "energy on disguises!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF78)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 5900, 30600, 0)
    MoveCamera(10, 20, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(13150, 0)
    OP_0D()
    Sound(540, 0, 50, 0)
    Sound(531, 0, 50, 0)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x4A)
    OP_A0(0x10, 1500, 0x0, 0x1)
    Sleep(500)
    Sound(809, 0, 60, 0)
    OP_A0(0x10, 1500, 0x2, 0x3)
    SetChrSubChip(0x10, 0x4)
    OP_68(-950, 4550, 25250, 800)
    MoveCamera(359, -8, 0, 800)
    SetCameraDistance(18300, 800)
    ClearChrFlags(0x29, 0x80)
    Sound(926, 2, 100, 0)
    BeginChrThread(0x29, 3, 0, 37)
    OP_9D(0x29, 0xFFFFFC18, 0x320, 0x5366, 0x5DC, 0x1388)
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    EndChrThread(0x29, 0x3)
    SetChrSubChip(0x29, 0x7)
    Sound(645, 0, 100, 0)
    Sound(308, 0, 100, 0)
    Sound(540, 0, 50, 0)
    OP_24(0x39E)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x9, 0x2)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x10,
        (
            "#04604F#11PI brought that from your\x01",
            "room, Rixia!\x02\x03",
            "#04602FThe greatest stage is\x01",
            "ready! Let's dance our\x01",
            "hearts out, Rixia!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1700, 20500, 1000)
    MoveCamera(0, 10, 0, 1000)
    SetCameraDistance(13300, 1000)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x41)
    SetChrSubChip(0x9, 0x0)
    OP_96(0x9, 0xFFFFFA24, 0x4B0, 0x5014, 0x3E8, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x43)
    SetChrSubChip(0x9, 0x0)
    OP_6F(0x79)
    Fade(250)
    Sound(308, 0, 100, 0)
    SetChrFlags(0x29, 0x80)
    OP_A0(0x9, 1500, 0x1, 0x2)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    OP_68(-950, 3550, 25250, 800)
    MoveCamera(5, -2, -5, 800)
    OP_6E(500, 800)
    SetCameraDistance(16370, 800)
    Sleep(100)
    OP_A0(0x9, 2000, 0x3, 0x4)
    Sleep(500)
    BeginChrThread(0x9, 0, 0, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#06215F#3253V#6P#32A#N#40WI'll never forgive you...!!#800W!\x01",
            "#4S#30WShirley Orlandoooo!!!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    StopSound(868, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 0)
    Sleep(500)
    OP_24(0x366)
    OP_24(0x36B)
    OP_24(0x36D)
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x39E)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_575 end

    def Function_3_2C9E(): pass

    label("Function_3_2C9E")

    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x64, 0x64, 0x1388, 0x9C4)
    SetCameraDistance(18500, 4500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    CancelBlur(5000)
    Return()

    # Function_3_2C9E end

    def Function_4_2CE1(): pass

    label("Function_4_2CE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CF9")
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x2)
    Jump("Function_4_2CE1")

    label("loc_2CF9")

    Return()

    # Function_4_2CE1 end

    def Function_5_2CFA(): pass

    label("Function_5_2CFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D12")
    OP_A1(0xFE, 0xDAC, 0x2, 0x4, 0x5)
    Jump("Function_5_2CFA")

    label("loc_2D12")

    Return()

    # Function_5_2CFA end

    def Function_6_2D13(): pass

    label("Function_6_2D13")

    OP_95(0x9, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0x9, -1800, 1250, 22700, 4000, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Return()

    # Function_6_2D13 end

    def Function_7_2D43(): pass

    label("Function_7_2D43")

    OP_95(0x9, -1800, 1250, 21400, 4000, 0x0)
    OP_95(0x9, -1850, 1250, 22500, 4000, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Return()

    # Function_7_2D43 end

    def Function_8_2D73(): pass

    label("Function_8_2D73")

    OP_95(0x9, -1350, 1250, 21700, 4000, 0x0)
    OP_95(0x9, -1800, 1250, 19850, 4000, 0x0)
    TurnDirection(0x9, 0xC, 500)
    Return()

    # Function_8_2D73 end

    def Function_9_2DA3(): pass

    label("Function_9_2DA3")

    OP_95(0xB, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xB, -1450, 1250, 21550, 4000, 0x0)
    OP_95(0xB, -750, 1250, 22250, 4000, 0x0)
    OP_93(0xB, 0x0, 0x1F4)
    Return()

    # Function_9_2DA3 end

    def Function_10_2DE7(): pass

    label("Function_10_2DE7")

    OP_95(0xB, -1850, 1250, 21700, 4000, 0x0)
    OP_93(0xB, 0x13B, 0x1F4)
    Return()

    # Function_10_2DE7 end

    def Function_11_2E03(): pass

    label("Function_11_2E03")

    OP_95(0xC, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xC, -2800, 1250, 23300, 4000, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)
    Return()

    # Function_11_2E03 end

    def Function_12_2E33(): pass

    label("Function_12_2E33")

    OP_95(0xC, -3000, 1250, 22400, 4000, 0x0)
    OP_93(0xC, 0x87, 0x1F4)
    Return()

    # Function_12_2E33 end

    def Function_13_2E4F(): pass

    label("Function_13_2E4F")

    OP_95(0xD, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xD, -5100, 1250, 21950, 4000, 0x0)
    TurnDirection(0xD, 0x8, 500)
    Return()

    # Function_13_2E4F end

    def Function_14_2E7F(): pass

    label("Function_14_2E7F")

    OP_95(0xD, -9000, 1250, 25400, 4000, 0x0)
    OP_95(0xD, -12000, 1250, 25400, 4000, 0x0)
    Return()

    # Function_14_2E7F end

    def Function_15_2EA8(): pass

    label("Function_15_2EA8")

    OP_95(0xF, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xF, -3900, 1250, 23450, 4000, 0x0)
    TurnDirection(0xF, 0x8, 500)
    Return()

    # Function_15_2EA8 end

    def Function_16_2ED8(): pass

    label("Function_16_2ED8")

    OP_95(0xF, -9000, 1250, 25400, 4000, 0x0)
    OP_95(0xF, -12000, 1250, 25400, 4000, 0x0)
    Return()

    # Function_16_2ED8 end

    def Function_17_2F01(): pass

    label("Function_17_2F01")

    OP_95(0xE, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xE, -4850, 1250, 23450, 4000, 0x0)
    TurnDirection(0xE, 0x8, 500)
    Return()

    # Function_17_2F01 end

    def Function_18_2F31(): pass

    label("Function_18_2F31")

    OP_95(0xE, -9000, 1250, 25400, 4000, 0x0)
    OP_95(0xE, -12000, 1250, 25400, 4000, 0x0)
    Return()

    # Function_18_2F31 end

    def Function_19_2F5A(): pass

    label("Function_19_2F5A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FA9")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 800, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x3, 0x2)
    Jump("Function_19_2F5A")

    label("loc_2FA9")

    Return()

    # Function_19_2F5A end

    def Function_20_2FAA(): pass

    label("Function_20_2FAA")

    ClearChrFlags(0x11, 0x4)
    OP_95(0x11, 600, 0, 15250, 6000, 0x0)
    OP_95(0x11, 7000, 0, 17750, 6000, 0x0)
    OP_93(0x11, 0x87, 0x1F4)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 0x4C)
    OP_A1(0x11, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_20_2FAA end

    def Function_21_2FF0(): pass

    label("Function_21_2FF0")

    ClearChrFlags(0x12, 0x4)
    OP_95(0x12, -600, 0, 15250, 6000, 0x0)
    OP_95(0x12, -7000, 0, 17750, 6000, 0x0)
    OP_93(0x12, 0xE1, 0x1F4)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x4C)
    OP_A1(0x12, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_21_2FF0 end

    def Function_22_3036(): pass

    label("Function_22_3036")

    ClearChrFlags(0x13, 0x4)
    OP_95(0x13, 600, 0, 15250, 6000, 0x0)
    OP_95(0x13, 3600, 0, 16000, 6000, 0x0)
    OP_93(0x13, 0xB4, 0x1F4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 0x4C)
    OP_A1(0x13, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_22_3036 end

    def Function_23_307C(): pass

    label("Function_23_307C")

    ClearChrFlags(0x14, 0x4)
    OP_95(0x14, -600, 0, 15250, 6000, 0x0)
    OP_95(0x14, -3600, 0, 16000, 6000, 0x0)
    OP_93(0x14, 0xB4, 0x1F4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 0x4C)
    OP_A1(0x14, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_23_307C end

    def Function_24_30C2(): pass

    label("Function_24_30C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3111")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 0, 2200, 0, 270, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x0)
    Jump("Function_24_30C2")

    label("loc_3111")

    Return()

    # Function_24_30C2 end

    def Function_25_3112(): pass

    label("Function_25_3112")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3161")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 0, 2200, 0, 270, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x5, 0x4)
    Jump("Function_25_3112")

    label("loc_3161")

    Return()

    # Function_25_3112 end

    def Function_26_3162(): pass

    label("Function_26_3162")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B1")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 200, 0, 2200, 0, 270, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x3, 0x2)
    Jump("Function_26_3162")

    label("loc_31B1")

    Return()

    # Function_26_3162 end

    def Function_27_31B2(): pass

    label("Function_27_31B2")

    OP_93(0xFE, 0xB4, 0x2EE)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_27_31B2 end

    def Function_28_31D3(): pass

    label("Function_28_31D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31FF")
    OP_95(0xFE, 850, 2250, 3000, 4000, 0x0)
    Jump("loc_3213")

    label("loc_31FF")

    OP_95(0xFE, 0, 2250, 3000, 4000, 0x0)

    label("loc_3213")

    Call(0, 27)
    Return()

    # Function_28_31D3 end

    def Function_29_3217(): pass

    label("Function_29_3217")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3243")
    OP_95(0xFE, -850, 2250, 3000, 4000, 0x0)
    Jump("loc_3257")

    label("loc_3243")

    OP_95(0xFE, 0, 2250, 3000, 4000, 0x0)

    label("loc_3257")

    Call(0, 27)
    Return()

    # Function_29_3217 end

    def Function_30_325B(): pass

    label("Function_30_325B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3287")
    OP_95(0xFE, 850, 1800, 5350, 4000, 0x0)
    Jump("loc_329B")

    label("loc_3287")

    OP_95(0xFE, 0, 1800, 5350, 4000, 0x0)

    label("loc_329B")

    Call(0, 27)
    Return()

    # Function_30_325B end

    def Function_31_329F(): pass

    label("Function_31_329F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CB")
    OP_95(0xFE, -850, 1800, 5350, 4000, 0x0)
    Jump("loc_32DF")

    label("loc_32CB")

    OP_95(0xFE, 0, 1800, 5350, 4000, 0x0)

    label("loc_32DF")

    Call(0, 27)
    Return()

    # Function_31_329F end

    def Function_32_32E3(): pass

    label("Function_32_32E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_330F")
    OP_95(0xFE, 850, 1350, 7600, 4000, 0x0)
    Jump("loc_3323")

    label("loc_330F")

    OP_95(0xFE, 0, 1350, 7600, 4000, 0x0)

    label("loc_3323")

    Call(0, 27)
    Return()

    # Function_32_32E3 end

    def Function_33_3327(): pass

    label("Function_33_3327")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3353")
    OP_95(0xFE, -850, 1350, 7600, 4000, 0x0)
    Jump("loc_3367")

    label("loc_3353")

    OP_95(0xFE, 0, 1350, 7600, 4000, 0x0)

    label("loc_3367")

    Call(0, 27)
    Return()

    # Function_33_3327 end

    def Function_34_336B(): pass

    label("Function_34_336B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3397")
    OP_95(0xFE, 850, 900, 9900, 4000, 0x0)
    Jump("loc_33AB")

    label("loc_3397")

    OP_95(0xFE, 0, 900, 9900, 4000, 0x0)

    label("loc_33AB")

    Call(0, 27)
    Return()

    # Function_34_336B end

    def Function_35_33AF(): pass

    label("Function_35_33AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33DB")
    OP_95(0xFE, -850, 900, 9900, 4000, 0x0)
    Jump("loc_33EF")

    label("loc_33DB")

    OP_95(0xFE, 0, 900, 9900, 4000, 0x0)

    label("loc_33EF")

    Call(0, 27)
    Return()

    # Function_35_33AF end

    def Function_36_33F3(): pass

    label("Function_36_33F3")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -4250, 1250, 23150)
    OP_9F(0x1, -5350, 1250, 23950)
    OP_9F(0x1, -6450, 1250, 24400)
    OP_9F(0x1, -7850, 1250, 24650)
    OP_9F(0x1, -12000, 1250, 25400)
    OP_9F(0x2, 0xFE, 1000, 0x0)
    Return()

    # Function_36_33F3 end

    def Function_37_3447(): pass

    label("Function_37_3447")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_345E")
    OP_A0(0xFE, 6000, 0x8, 0xF)
    Jump("Function_37_3447")

    label("loc_345E")

    Return()

    # Function_37_3447 end

    def Function_38_345F(): pass

    label("Function_38_345F")

    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, 0, 2000, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4500, 3200, 20000, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4500, 3200, 20000, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4500, 31100, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4100, 4500, 31100, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x7D0)
    SetChrPos(0xA, -2500, 1250, 25450, 225)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    BeginChrThread(0xA, 3, 0, 47)

    def lambda_35ED():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x14B4, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_35ED)
    Sleep(1200)
    BeginChrThread(0xA, 0, 0, 40)
    Sleep(25000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_345F end

    def Function_39_3641(): pass

    label("Function_39_3641")

    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x226)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)

    def lambda_3752():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x53C, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3752)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 0x37)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xE1, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1250)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x3E8)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    BeginChrThread(0xA, 3, 0, 47)

    def lambda_3BBD():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3BBD)
    Sleep(250)

    def lambda_3BDB():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3BDB)
    Sleep(250)

    def lambda_3BF9():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3BF9)
    Sleep(250)

    def lambda_3C17():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3C17)
    Return()

    # Function_39_3641 end

    def Function_40_3C2E(): pass

    label("Function_40_3C2E")


    def lambda_3C33():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3C33)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 45)
    Sleep(1000)

    def lambda_3C60():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3C60)
    OP_49()
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xA, 0x2)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    def lambda_3E06():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3E06)
    OP_49()
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xA, 0x3)

    def lambda_3EE8():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3EE8)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_3FC7():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3FC7)
    OP_49()
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0xAF)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0x10E, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0xBB8, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Sleep(700)
    OP_68(0, 2900, 25220, 4500)
    MoveCamera(-5, 15, -1, 4500)
    SetCameraDistance(15000, 4500)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x7D0, 0x4E2, 0x61A8, 0x1194, 0x0)
    BeginChrThread(0xA, 1, 0, 41)
    OP_9D(0xA, 0x3E8, 0x4E2, 0x61A8, 0x3E8, 0xBB8)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 46)
    OP_9D(0xA, 0x0, 0x4E2, 0x61A8, 0x5DC, 0xBB8)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 45)
    OP_9D(0xA, 0xFFFFF92A, 0x4E2, 0x61A8, 0x7D0, 0xBB8)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_444C():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_444C)
    OP_9D(0xA, 0xFFFFF060, 0x4E2, 0x61A8, 0xBB8, 0x578)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(500)
    EndChrThread(0xA, 0x3)
    SetChrChip(0x0, 0xA, 0xBB8, 0x12C)
    Sleep(400)
    OP_68(0, 4900, 25220, 7000)
    MoveCamera(0, -10, 0, 7000)
    SetCameraDistance(15000, 7000)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 2, 0, 45)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x7D0, 0x8FC)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 46)
    OP_96(0xA, 0xFFFFF830, 0x4E2, 0x6590, 0x1B58, 0x0)
    OP_9E(0xA, 0xFFFFFE0C, 0x61A8, 0x2BF20, 0x2328, 0x0)
    BeginChrThread(0xA, 1, 0, 45)
    OP_9E(0xA, 0xC8, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0xFFFFFF06, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0x32, 0x61A8, 0x7A120, 0x2328, 0x0)
    BeginChrThread(0xA, 2, 0, 54)
    OP_9D(0xA, 0x0, 0x4E2, 0x639C, 0xFA0, 0x514)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x1)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x3)
    Return()

    # Function_40_3C2E end

    def Function_41_488F(): pass

    label("Function_41_488F")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_41_488F end

    def Function_42_48B3(): pass

    label("Function_42_48B3")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_42_48B3 end

    def Function_43_48D7(): pass

    label("Function_43_48D7")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x9C4, 0x2, 0x0, 0x1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_48D7 end

    def Function_44_48EC(): pass

    label("Function_44_48EC")

    SetChrChipByIndex(0xFE, 0x3B)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_44_48EC end

    def Function_45_48FA(): pass

    label("Function_45_48FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4918")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_45_48FA")

    label("loc_4918")

    Return()

    # Function_45_48FA end

    def Function_46_4919(): pass

    label("Function_46_4919")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4937")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(60)
    Jump("Function_46_4919")

    label("loc_4937")

    Return()

    # Function_46_4919 end

    def Function_47_4938(): pass

    label("Function_47_4938")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4982")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_47_4938")

    label("loc_4982")

    Return()

    # Function_47_4938 end

    def Function_48_4983(): pass

    label("Function_48_4983")

    Sound(877, 2, 10, 0)
    Sleep(100)
    OP_25(0x36D, 0x14)
    Sleep(100)
    OP_25(0x36D, 0x1E)
    Sleep(100)
    OP_25(0x36D, 0x28)
    Sleep(100)
    OP_25(0x36D, 0x32)
    Sleep(100)
    OP_25(0x36D, 0x3C)
    Sleep(100)
    OP_25(0x36D, 0x46)
    Sleep(100)
    OP_25(0x36D, 0x50)
    Sleep(100)
    OP_25(0x36D, 0x5A)
    Sleep(100)
    OP_25(0x36D, 0x64)
    Return()

    # Function_48_4983 end

    def Function_49_49C9(): pass

    label("Function_49_49C9")

    Sleep(500)
    Sound(818, 0, 60, 0)
    Sleep(8000)
    Sound(819, 0, 100, 0)
    Return()

    # Function_49_49C9 end

    def Function_50_49DC(): pass

    label("Function_50_49DC")

    Sleep(1000)
    Sound(818, 0, 100, 0)
    Sleep(10000)
    Sound(819, 0, 100, 0)
    Sleep(6000)
    Sound(819, 0, 100, 0)
    Return()

    # Function_50_49DC end

    def Function_51_49F8(): pass

    label("Function_51_49F8")

    LoadEffect(0x0, "event/ev15001.eff")
    LoadEffect(0x1, "event/ev15002.eff")
    CreatePortrait(0, 0, 0, 440, 40, 20, 217, 512, 128, 0, 0, 440, 40, 0xFFFFFF, 0x0, "c_mini00.itp")
    CreatePortrait(1, 0, 0, 20, 10, 80, 232, 512, 128, 0, 50, 20, 60, 0xFFFFFF, 0x0, "c_mini00.itp")
    CreatePortrait(2, 0, 0, 20, 10, 380, 232, 512, 128, 0, 80, 20, 90, 0xFFFFFF, 0x0, "c_mini00.itp")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0xA, 0, 1250, 25500, 225)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 3300, 24000, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Match with Sully's landing timing\x01",
            "and press the "○ button"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(1000)
    OP_E5(0xA)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7576", 1)
    Sleep(3000)
    FadeToBright(6000, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1770, 0x0, 0x0)
    Sleep(6000)
    SetChrChipByIndex(0xA, 0x39)
    Fade(500)
    SetChrSubChip(0xA, 0x0)
    Sleep(1400)
    BeginChrThread(0x3, 1, 0, 55)
    BeginChrThread(0x3, 2, 0, 56)
    BeginChrThread(0xA, 0, 0, 52)
    Sleep(10000)
    BeginChrThread(0xA, 0, 0, 53)
    Sleep(25000)
    Sleep(3000)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(2500, 0, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_0D()
    OP_E5(0xB)
    StopEffect(0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    OP_CC(0x1, 0x2, 0x0)
    Return()

    # Function_51_49F8 end

    def Function_52_4C6A(): pass

    label("Function_52_4C6A")

    Sound(809, 0, 40, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x44C)
    SetChrChipByIndex(0xA, 0x37)

    def lambda_4C9B():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0xA96, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4C9B)
    OP_49()
    Sound(809, 0, 40, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    Sound(809, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    Sound(809, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    Sound(809, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xE1, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1250)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)

    def lambda_4D77():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4D77)
    Sleep(250)

    def lambda_4D95():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4D95)
    Sleep(250)

    def lambda_4DB3():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4DB3)
    Sleep(250)

    def lambda_4DD1():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4DD1)
    Return()

    # Function_52_4C6A end

    def Function_53_4DE8(): pass

    label("Function_53_4DE8")


    def lambda_4DED():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4DED)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 45)
    Sleep(1000)

    def lambda_4E1A():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4E1A)
    OP_49()
    Sound(844, 0, 40, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0xA, 0x2)
    Sound(809, 0, 40, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(844, 0, 40, 0)

    def lambda_4E7A():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4E7A)
    OP_49()
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    Sound(809, 0, 40, 0)

    def lambda_4EB3():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4EB3)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(844, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_4EE9():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4EE9)
    OP_49()
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0xAF)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0x10E, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0xBB8, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Sleep(700)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x7D0, 0x4E2, 0x61A8, 0x1194, 0x0)
    BeginChrThread(0xA, 1, 0, 41)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0x3E8, 0x4E2, 0x61A8, 0x3E8, 0xBB8)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 46)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x61A8, 0x5DC, 0xBB8)
    BeginChrThread(0xA, 1, 0, 45)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0xFFFFF92A, 0x4E2, 0x61A8, 0x7D0, 0xBB8)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_4FE1():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4FE1)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0xFFFFF060, 0x4E2, 0x61A8, 0xBB8, 0x578)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(500)
    EndChrThread(0xA, 0x3)
    SetChrChip(0x0, 0xA, 0xBB8, 0x12C)
    Sleep(400)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 2, 0, 45)
    Sound(809, 0, 40, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x7D0, 0x8FC)
    Sleep(900)
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 46)
    OP_96(0xA, 0xFFFFF830, 0x4E2, 0x6590, 0x1B58, 0x0)
    OP_9E(0xA, 0xFFFFFE0C, 0x61A8, 0x2BF20, 0x2328, 0x0)
    BeginChrThread(0xA, 1, 0, 45)
    OP_9E(0xA, 0xC8, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0xFFFFFF06, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0x32, 0x61A8, 0x7A120, 0x2328, 0x0)
    BeginChrThread(0xA, 2, 0, 54)
    Sound(844, 0, 40, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x639C, 0xFA0, 0x514)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x1)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(1000)
    EndChrThread(0xA, 0x3)
    StopBGM(0x7D0)
    Return()

    # Function_53_4DE8 end

    def Function_54_5111(): pass

    label("Function_54_5111")

    OP_D5(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D5(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_54_5111 end

    def Function_55_5142(): pass

    label("Function_55_5142")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_517D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_578B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4E2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4E3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_577A")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5770")
    OP_64(0xA)
    OP_63(0xA, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sound(1028, 0, 100, 0)
    Sound(3, 0, 100, 0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xA, 0x3)
    SetChrChip(0x0, 0xA, 0xBB8, 0x12C)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524B")
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x64, 0x0, 0x0)
    Jump("loc_5763")

    label("loc_524B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5298")
    OP_CB(0x2, 0x1, 0x7D0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x57E40, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x28, 0x5A)
    Jump("loc_5763")

    label("loc_5298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52E5")
    OP_CB(0x2, 0x1, 0xBB8, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x53020, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x3C, 0x5A)
    Jump("loc_5763")

    label("loc_52E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5332")
    OP_CB(0x2, 0x1, 0xFA0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x4E200, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x50, 0x5A)
    Jump("loc_5763")

    label("loc_5332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537F")
    OP_CB(0x2, 0x1, 0x1388, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x493E0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x64, 0x5A)
    Jump("loc_5763")

    label("loc_537F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53CC")
    OP_CB(0x2, 0x1, 0x1770, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x445C0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x78, 0x5A)
    Jump("loc_5763")

    label("loc_53CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5419")
    OP_CB(0x2, 0x1, 0x1B58, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x3F7A0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x8C, 0x5A)
    Jump("loc_5763")

    label("loc_5419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5466")
    OP_CB(0x2, 0x1, 0x1F40, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x3A980, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xA0, 0x5A)
    Jump("loc_5763")

    label("loc_5466")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B3")
    OP_CB(0x2, 0x1, 0x2328, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x35B60, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xB4, 0x5A)
    Jump("loc_5763")

    label("loc_54B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5500")
    OP_CB(0x2, 0x1, 0x2710, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x30D40, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xC8, 0x5A)
    Jump("loc_5763")

    label("loc_5500")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554D")
    OP_CB(0x2, 0x1, 0x2AF8, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x2BF20, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xDC, 0x5A)
    Jump("loc_5763")

    label("loc_554D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_559A")
    OP_CB(0x2, 0x1, 0x2EE0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x27100, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xF0, 0x5A)
    Jump("loc_5763")

    label("loc_559A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E7")
    OP_CB(0x2, 0x1, 0x32C8, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x222E0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x104, 0x5A)
    Jump("loc_5763")

    label("loc_55E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5634")
    OP_CB(0x2, 0x1, 0x36B0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x1D4C0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x118, 0x5A)
    Jump("loc_5763")

    label("loc_5634")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5681")
    OP_CB(0x2, 0x1, 0x3A98, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x186A0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x12C, 0x5A)
    Jump("loc_5763")

    label("loc_5681")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56CE")
    OP_CB(0x2, 0x1, 0x3E80, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x13880, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x140, 0x5A)
    Jump("loc_5763")

    label("loc_56CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571B")
    OP_CB(0x2, 0x1, 0x4268, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xEA60, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x154, 0x5A)
    Jump("loc_5763")

    label("loc_571B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5763")
    OP_CB(0x2, 0x1, 0x4650, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x9C40, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x168, 0x5A)

    label("loc_5763")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)

    label("loc_5770")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_577A")

    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_517D")

    label("loc_578B")

    Return()

    # Function_55_5142 end

    def Function_56_578C(): pass

    label("Function_56_578C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D0A")
    OP_57(0x3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0xA), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x8), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5CEB")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sound(1027, 0, 100, 0)
    Sound(87, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 3, 0, 47)
    SetChrChip(0x0, 0xA, 0x12C, 0xBB8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5904")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    Jump("loc_5CD9")

    label("loc_5904")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_593E")
    OP_CB(0x1, 0x1, 0x7D0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x28, 0x3C)
    Jump("loc_5CD9")

    label("loc_593E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5978")
    OP_CB(0x1, 0x1, 0xBB8, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x3C, 0x3C)
    Jump("loc_5CD9")

    label("loc_5978")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B2")
    OP_CB(0x1, 0x1, 0xFA0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x50, 0x3C)
    Jump("loc_5CD9")

    label("loc_59B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59EC")
    OP_CB(0x1, 0x1, 0x1388, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x64, 0x3C)
    Jump("loc_5CD9")

    label("loc_59EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A26")
    OP_CB(0x1, 0x1, 0x1770, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x78, 0x3C)
    Jump("loc_5CD9")

    label("loc_5A26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A60")
    OP_CB(0x1, 0x1, 0x1B58, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x8C, 0x3C)
    Jump("loc_5CD9")

    label("loc_5A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A9A")
    OP_CB(0x1, 0x1, 0x1F40, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xA0, 0x3C)
    Jump("loc_5CD9")

    label("loc_5A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD4")
    OP_CB(0x1, 0x1, 0x2328, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xB4, 0x3C)
    Jump("loc_5CD9")

    label("loc_5AD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B0E")
    OP_CB(0x1, 0x1, 0x2710, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xC8, 0x3C)
    Jump("loc_5CD9")

    label("loc_5B0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B48")
    OP_CB(0x1, 0x1, 0x2AF8, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xDC, 0x3C)
    Jump("loc_5CD9")

    label("loc_5B48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B82")
    OP_CB(0x1, 0x1, 0x2EE0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xF0, 0x3C)
    Jump("loc_5CD9")

    label("loc_5B82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BBC")
    OP_CB(0x1, 0x1, 0x32C8, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x104, 0x3C)
    Jump("loc_5CD9")

    label("loc_5BBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BF6")
    OP_CB(0x1, 0x1, 0x36B0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x118, 0x3C)
    Jump("loc_5CD9")

    label("loc_5BF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C30")
    OP_CB(0x1, 0x1, 0x3A98, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x12C, 0x3C)
    Jump("loc_5CD9")

    label("loc_5C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C6A")
    OP_CB(0x1, 0x1, 0x3E80, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x140, 0x3C)
    Jump("loc_5CD9")

    label("loc_5C6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CA4")
    OP_CB(0x1, 0x1, 0x4268, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x154, 0x3C)
    Jump("loc_5CD9")

    label("loc_5CA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD9")
    OP_CB(0x1, 0x1, 0x4650, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x168, 0x3C)

    label("loc_5CD9")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(300)
    Jump("loc_5D02")

    label("loc_5CEB")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    label("loc_5D02")

    Sleep(1)
    Jump("Function_56_578C")

    label("loc_5D0A")

    Return()

    # Function_56_578C end

    def Function_57_5D0B(): pass

    label("Function_57_5D0B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10000.itc", 0x1E)
    LoadChrToIndex("chr/ch09700.itc", 0x1F)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -540, 1250, 24890, 225)
    OP_68(-1550, 2500, 23490, 0)
    MoveCamera(354, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetChrPos(0x101, -1800, 1250, 23000, 45)
    SetChrPos(0x102, -1280, 1250, 22120, 45)
    SetChrPos(0x103, -2680, 1250, 23520, 45)
    SetChrPos(0x104, -2700, 1250, 21400, 45)
    SetChrPos(0x109, -2180, 1250, 20520, 45)
    SetChrPos(0x105, -3580, 1250, 21920, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    LoadChrToIndex("chr/ch14100.itc", 0x3C)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#12203FThen, allow me to\x01",
            "explain immediately.\x02\x03",
            "#12201FTake this first.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xA, 0x101, 0x4B0, 0x7D0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd received a\x01",
            "whistle.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_96(0xA, 0xFFFFFDE4, 0x4E2, 0x613A, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00005FThis is... a whistle?\x01",
            "What do I use it for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FStarting now, I'll perform as if\x01",
            "were the real thing...\x02\x03",
            "#12201FDuring my performance, I want you\x01",
            "to blow that whistle on the\x01",
            "landing of each of my jumps.\x02\x03",
            "Even if you don't know how it\x01",
            "goes, you should be able to follow\x01",
            "my movements with your eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see, the landings...\x02\x03",
            "#00005FWait, are you ok with\x01",
            "just that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FYeah, it's simple, but really\x01",
            "important.\x02\x03",
            "#12201FIn Arc-en-Ciel performances,\x01",
            "jumps are essential, to say the\x01",
            "least.\x02\x03",
            ""Landing" in particular is an\x01",
            "important base action which\x01",
            "leads into all other movements.\x02\x03",
            "The whistle is a cue to raise\x01",
            "awareness.\x02\x03",
            "#12206FSo that's why you'll never blow\x01",
            "it with an odd timing, ok?\x01",
            "That'll confuse me instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FGot it, I'll be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12200FSo, explanation's over.\x01",
            "Are you ready to begin\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'm ready when you\x01",
            "are.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    BeginChrThread(0x0, 0, 0, 51)
    WaitChrThread(0x0, 0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x1020)
    SetChrPos(0xA, 0, 1250, 25500, 225)
    SetChrPos(0x101, -1800, 1250, 23000, 45)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x105, 0x80)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    OP_68(-1200, 2500, 24000, 0)
    MoveCamera(354, 18, 1, 0)
    OP_6E(460, 0)
    SetCameraDistance(19290, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#12206FPhew, I guess it took\x01",
            "form somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWell, as for the form,\x01",
            "you were great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYes, you really were.\x01",
            "You should have more\x01",
            "confidence.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651F")
    OP_2C(0x8D, 0x2)
    OP_29(0x8D, 0x1, 0x0)

    ChrTalk(
        0xA,
        (
            "#12212FT-Thanks...\x02\x03",
            "#12202FEven so, to think you matched my\x01",
            "movements perfectly... you're\x01",
            "good.\x02\x03",
            "Thanks to you I was able to quite\x01",
            "sense the connections. It turned\x01",
            "into a pretty solid training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, if you're saying\x01",
            "that much I guess it was\x01",
            "most satisfactory.\x02\x03",
            "I'm just glad I could\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66F5")

    label("loc_651F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65E6")
    OP_2C(0x8D, 0x1)
    OP_29(0x8D, 0x1, 0x1)

    ChrTalk(
        0xA,
        (
            "#12212FT-Thanks...\x02\x03",
            "#12200FWell, the whistle timing\x01",
            "was a bit weird, but...\x02\x03",
            "Even so, it turned into\x01",
            "a pretty solid training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI see, that's good then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_66F5")

    label("loc_65E6")

    OP_29(0x8D, 0x1, 0x2)

    ChrTalk(
        0xA,
        (
            "#12212FT-Thanks...\x02\x03",
            "#12206FBut your whistling was\x01",
            "honestly no good at all.\x02\x03",
            "Conversely, I've gotten\x01",
            "used to the correct timing,\x01",
            "so I sort of know it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FY-Yeah, I'm ashamed.\x02\x03",
            "#00008F(Following her movements\x01",
            "with the eyes? It's\x01",
            "harder than I thought.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F5")


    ChrTalk(
        0xA,
        (
            "#12203FSo, here's the main\x01",
            "question...\x02\x03",
            "#12201FYou saw my acting.\x01",
            "So...how was it...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-1800, 2500, 23700, 0)
    MoveCamera(260, 21, 1, 0)
    OP_6E(560, 0)
    SetCameraDistance(14730, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FUhmm...\x02\x03",
            "Well, what can I say? I thought\x01",
            "it was simply great.\x02\x03",
            "To think you could make a\x01",
            "performance of that level your\x01",
            "own...\x02\x03",
            "#00006FBut, I'm sorry. I guess an\x01",
            "amateur like me can't really say\x01",
            "anything more sensible than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FI see...\x02\x03",
            "#12201FSo, about what you told me in\x01",
            "the beginning, that my acting\x01",
            "has no wasted movements...\x02\x03",
            "Could you tell me in detail\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FDid I... say something\x01",
            "like that?\x02\x03",
            "#00006FWell, I didn't mean it\x01",
            "in a bad way at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203F............\x02\x03",
            "#12208F...Actually, Ilya said\x01",
            "the same thing once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12208FThere's no wasted\x01",
            "movements in your\x01",
            "acting...\x02\x03",
            "Your acting is\x01",
            "serious...\x02\x03",
            "#12206FAlso... she told me to\x01",
            "enjoy it more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FTo enjoy it, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIlya told you that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, but in that sense,\x01",
            "there's no big problem\x01",
            "in practice...\x02\x03",
            "#10300FIf I had to say,\x01",
            "couldn't it be all in\x01",
            "your head?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#12211FWhat, in my head!? I don't\x01",
            "get it at all!\x02\x03",
            "#12208F............\x02\x03",
            "#12206FStill, at this rate... I'm\x01",
            "sure tomorrow's\x01",
            "performance won't go well.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x103,
        "#00201FSully...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)

    ChrTalk(
        0x101,
        (
            "#00003F...Say, Sully. There's\x01",
            "something I'd like to\x01",
            "know.\x02\x03",
            "#00001FWhat do you think about\x01",
            "during performance\x01",
            "training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12205FEh, huh?\x02\x03",
            "#12201FAin't it obvious I'm\x01",
            "thinking I want to get\x01",
            "better?\x02\x03",
            "#12208F...No, it's a bit\x01",
            "different.\x02\x03",
            "I think... I want to\x01",
            "perform like Ilya and\x01",
            "Rixia.\x02\x03",
            "#12201FI want it to feel like it\x01",
            "did when I saw them perform\x01",
            "for the first time.\x02\x03",
            "How can I say it, like\x01",
            "grabbing their hearts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FSully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThat's a rather direct\x01",
            "was of putting it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "#12211FI-I didn't intend to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... Then, what about\x01",
            "these questions?\x02\x03",
            "#00001FWhat do you think when you\x01",
            "act on the Arc-en-Ciel stage?\x02\x03",
            "What do you think about the\x01",
            "audience that has come to the\x01",
            "theater to see you perform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12201F...The audience? Oh, the\x01",
            "audience, huh?\x02\x03",
            "#12208FI recently learned there all\x01",
            "kinds of guys in this city,\x01",
            "but...\x02\x03",
            "Even so, I can't really like\x01",
            "those who haven't realized\x01",
            "how fortunate they are.\x02\x03",
            "#12201FI won't say our entire\x01",
            "audience is like that... but\x01",
            "most of them are.\x02\x03",
            "So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FSo... You can't think it's\x01",
            "a good thing for them to\x01",
            "see your performance?\x02\x03",
            "...Basically, you're\x01",
            "saying you can't simply\x01",
            "enjoy acting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FHmm, well... That's just how I\x01",
            "feel.\x02\x03",
            "I try not to think about it, but\x01",
            "I get creeped out when I think\x01",
            "I'm acting for their sakes.\x02\x03",
            "#12201FBut, is that wrong? I mean,\x01",
            "those feelings have nothing to\x01",
            "do with my acting, right?\x02\x03",
            "I want to know more specifically\x01",
            "where and how I made mistakes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FFeelings and acting are\x01",
            "not related, huh?\x02\x03",
            "#00001FI wonder if that's\x01",
            "really true?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#12207FEven if you say that,\x01",
            "what, specifically,\x01",
            "should I do!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FWell... I'm not sure how\x01",
            "to put it, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 0, 1100, 8800, 360)

    NpcTalk(
        0x8,
        "Woman's Voice",
        (
            "...In that case Sully,\x01",
            "ignore the audience in\x01",
            "front of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    def lambda_73F9():

        label("loc_73F9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_73F9")

    QueueWorkItem2(0x109, 0, lambda_73F9)
    Sleep(50)

    def lambda_740E():

        label("loc_740E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_740E")

    QueueWorkItem2(0x102, 0, lambda_740E)
    Sleep(50)

    def lambda_7423():

        label("loc_7423")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7423")

    QueueWorkItem2(0x104, 0, lambda_7423)
    Sleep(50)

    def lambda_7438():

        label("loc_7438")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7438")

    QueueWorkItem2(0x101, 0, lambda_7438)
    Sleep(50)

    def lambda_744D():

        label("loc_744D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_744D")

    QueueWorkItem2(0x105, 0, lambda_744D)
    Sleep(50)

    def lambda_7462():

        label("loc_7462")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7462")

    QueueWorkItem2(0x103, 0, lambda_7462)
    Sleep(50)

    def lambda_7477():

        label("loc_7477")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7477")

    QueueWorkItem2(0xA, 0, lambda_7477)
    Fade(500)
    OP_68(-250, 2000, 21140, 0)
    MoveCamera(203, 15, 1, 0)
    OP_6E(460, 0)
    SetCameraDistance(17000, 0)
    Sleep(500)

    def lambda_74BF():
        OP_97(0xFE, 0x0, 0xFFFFF830, 0x2710, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_74BF)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-940, 2600, 21160, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18850, 0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 1600, 1250, 21090, 270)
    SetChrPos(0xA, 1600, 1250, 23000, 180)
    SetChrPos(0x102, -1800, 1250, 22800, 45)
    SetChrPos(0x101, -1800, 1250, 21500, 45)
    SetChrPos(0x103, -1800, 1250, 20200, 45)
    SetChrPos(0x105, -3000, 1250, 22800, 45)
    SetChrPos(0x104, -3000, 1250, 21500, 45)
    SetChrPos(0x109, -3000, 1250, 20200, 45)
    FadeToBright(1000, 0)
    Sleep(500)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0xA, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        "#06109FYoohoo, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIlya.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12207F#5P...Wait, how long have\x01",
            "you been here!?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(30, 2800, 20910, 2000)
    TurnDirection(0x8, 0xA, 500)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#06104FHmm? I just got there,\x01",
            "though.\x02\x03",
            "#06100FSo, Sully. You say you\x01",
            "hate our audience?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12208FHmph, is that so wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06104FNo, it actually isn't.\x02\x03",
            "There are customers even I\x01",
            "hate, to varying degrees.\x02\x03",
            "#06102FHowever, I can't very well\x01",
            "let each and every one of\x01",
            "the get to me, now can I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12201FI know that already. I'm\x01",
            "doing my best to not be\x01",
            "bothered by them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06106F*sigh*, in your case,\x01",
            "your way of thinking the\x01",
            "problem.\x02\x03",
            "#06102FListen, you're far too\x01",
            "concerned with what's in\x01",
            "front of you.\x02\x03",
            "Say Sully, do you know\x01",
            "what an "audience"\x01",
            "refers to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12201FYeah, it's the people who\x01",
            "come to the theatre. Those\x01",
            "who paid for a ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06103FWell, you're not wrong. But\x01",
            "there's something more\x01",
            "important.\x02\x03",
            "#06100FYour audience isn't just\x01",
            "those who come to the\x01",
            "theatre.\x02\x03",
            "The people who are interested\x01",
            "in our performances... All of\x01",
            "them are our audience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12205FAll the people who are\x01",
            "interested...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06103FRight, even the people who only saw\x01",
            "our troupe in magazines and even\x01",
            "those who have only heard of us.\x02\x03",
            "You could say all the people who\x01",
            "take an interest in us, no matter\x01",
            "the form, are our audience.\x02\x03",
            "#06102FYou know that too, right?\x02\x03",
            "You came to Crossbell, heard rumors\x01",
            "about Arc-en-Ciel...\x02\x03",
            "You snuck into the theatre, saw our\x01",
            "performance, and felt something,\x01",
            "right?\x02\x03",
            "Well, I won't praise you for\x01",
            "sneaking in, though.\x02\x03",
            "#06109FEven so, at that time, there's no\x01",
            "doubt that you were a splendid\x01",
            "customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12211FI who snuck in... was a\x01",
            "splendid customer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06100FThat's right. So don't be\x01",
            "so fixated on the audience\x01",
            "in front of you.\x02\x03",
            "#06109FAfter all, it's like we're\x01",
            "performing for all the\x01",
            "people of the continent.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12207FE-Everyone on the\x01",
            "continent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06102FHaha. It's true, isn't it.\x02\x03",
            "I can't say the name of Arc-en-Ciel\x01",
            "has spread throughout the continent\x01",
            "yet, but...\x02\x03",
            "#06104FEven so, through performance, you\x01",
            "of North Ambrian and I of\x01",
            "Crossbellian origins, connected.\x02\x03",
            "Maybe you think our meeting was a\x01",
            "coincidence... but I don't think\x01",
            "so.\x02\x03",
            "#06109FAll considered, don't you think\x01",
            "expressing yourself through\x01",
            "performance is fascinating and fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12205F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06104FHaha, oh well. Take your\x01",
            "time and think carefully\x01",
            "about it.\x02\x03",
            "#06101FThat aside, you didn't\x01",
            "even have breakfast this\x01",
            "morning, did you.\x02\x03",
            "There's a lunchbox in the\x01",
            "dressing room for you, so\x01",
            "go finish that now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12208FA l-lunchbox... I don't\x01",
            "really want it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06102FNope, I've told you many\x01",
            "times: Our bodies are\x01",
            "our capital.\x02\x03",
            "Training is on hold\x01",
            "until you've eaten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12201FTch, annoying as always.\x02\x03",
            "#12207FAlright, I'll be back\x01",
            "after I eat it!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1730, 3000, 20020, 2000)
    MoveCamera(45, 22, 0, 2000)
    OP_6E(480, 2000)
    SetCameraDistance(17010, 2000)

    def lambda_80BA():

        label("loc_80BA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_80BA")

    QueueWorkItem2(0x109, 0, lambda_80BA)

    def lambda_80CC():

        label("loc_80CC")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_80CC")

    QueueWorkItem2(0x102, 0, lambda_80CC)

    def lambda_80DE():

        label("loc_80DE")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_80DE")

    QueueWorkItem2(0x104, 0, lambda_80DE)

    def lambda_80F0():

        label("loc_80F0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_80F0")

    QueueWorkItem2(0x101, 0, lambda_80F0)

    def lambda_8102():

        label("loc_8102")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8102")

    QueueWorkItem2(0x105, 0, lambda_8102)

    def lambda_8114():

        label("loc_8114")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8114")

    QueueWorkItem2(0x103, 0, lambda_8114)

    def lambda_8126():

        label("loc_8126")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8126")

    QueueWorkItem2(0x8, 0, lambda_8126)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    OP_95(0xA, -2590, 1250, 25130, 7000, 0x0)
    OP_95(0xA, -8310, 1250, 25700, 7000, 0x0)

    def lambda_8169():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_8169)
    OP_95(0xA, -12090, 1250, 26230, 7000, 0x0)
    Sleep(1000)

    def lambda_8191():

        label("loc_8191")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_8191")

    QueueWorkItem2(0x109, 0, lambda_8191)

    def lambda_81A3():

        label("loc_81A3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_81A3")

    QueueWorkItem2(0x102, 0, lambda_81A3)

    def lambda_81B5():

        label("loc_81B5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_81B5")

    QueueWorkItem2(0x104, 0, lambda_81B5)

    def lambda_81C7():

        label("loc_81C7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_81C7")

    QueueWorkItem2(0x101, 0, lambda_81C7)

    def lambda_81D9():

        label("loc_81D9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_81D9")

    QueueWorkItem2(0x105, 0, lambda_81D9)

    def lambda_81EB():

        label("loc_81EB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_81EB")

    QueueWorkItem2(0x103, 0, lambda_81EB)
    Sleep(1000)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002FWhat can I say, that was\x01",
            "really a good scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYes, Ilya's words\x01",
            "penetrated my heart and\x01",
            "soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FAlso, well, you felt\x01",
            "like a mom.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#06109FHaha, right. Thanks to\x01",
            "her, it's never boring\x01",
            "around here.\x02\x03",
            "#06100FI should thank you guys\x01",
            "too.\x02\x03",
            "After all, I was able to\x01",
            "listen to that girl's\x01",
            "worries.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FBy any chance... Did you\x01",
            "watch everything from\x01",
            "the start?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06102FYes, perfectly, from the\x01",
            "shadows of the auditorium.\x02\x03",
            "#06103FI talk about a lot of\x01",
            "different things with that\x01",
            "girl, but...\x02\x03",
            "I don't actually get many\x01",
            "chances like this one to\x01",
            "hear what she really feels.\x02\x03",
            "#06109FI'm really grateful to you,\x01",
            "little bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FNo, don't say that...\x02\x03",
            "#00006FI couldn't give her any\x01",
            "advice, either.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8522():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_8522)
    SetChrPos(0xA, -8310, 1250, 25700, 90)
    Sound(809, 0, 70, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 41)
    OP_9D(0xA, 0xFFFFF312, 0x4E2, 0x5E10, 0x7D0, 0x1388)
    Sound(50, 0, 100, 0)
    OP_68(-1730, 3000, 20020, 2000)
    MoveCamera(33, 22, 0, 2000)
    OP_6E(480, 2000)
    SetCameraDistance(17010, 2000)

    def lambda_85A0():

        label("loc_85A0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_85A0")

    QueueWorkItem2(0x8, 2, lambda_85A0)

    def lambda_85B2():

        label("loc_85B2")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_85B2")

    QueueWorkItem2(0x105, 2, lambda_85B2)

    def lambda_85C4():

        label("loc_85C4")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_85C4")

    QueueWorkItem2(0x104, 2, lambda_85C4)

    def lambda_85D6():

        label("loc_85D6")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_85D6")

    QueueWorkItem2(0x101, 2, lambda_85D6)

    def lambda_85E8():

        label("loc_85E8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_85E8")

    QueueWorkItem2(0x109, 2, lambda_85E8)

    def lambda_85FA():

        label("loc_85FA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_85FA")

    QueueWorkItem2(0x102, 2, lambda_85FA)

    def lambda_860C():

        label("loc_860C")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_860C")

    QueueWorkItem2(0x103, 2, lambda_860C)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(500)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    OP_95(0xA, -810, 1250, 24380, 5000, 0x0)
    OP_95(0xA, 640, 1250, 22660, 5000, 0x0)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    TurnDirection(0xA, 0x8, 500)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#12201F#5PIlya, I've finished\x01",
            "eating.\x02",
        )
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00206F#5PWhat frightening speed,\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "#06106F*sigh*... And I always tell\x01",
            "you to chew before\x01",
            "swallowing... Oh, fine.\x02\x03",
            "#06100FAlright, we're continuing the\x01",
            "training.\x02\x03",
            "From the scene where the Star\x01",
            "Princess appears. I won't go\x01",
            "easy on you, you hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12202F#5PYeah, bring it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha. Sully looks fired\x01",
            "up somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, maybe she broke\x01",
            "through a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHaha, hope so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, let's excuse\x01",
            "ourselves for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FIlya, Sully, please do\x01",
            "your best with\x01",
            "tomorrow's performance.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0xA,
        "#12200F#2PS-Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06109FHaha, of course. See you\x01",
            "little bro, guys㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_6E(580, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Secret Acting\x01",
            "Coach]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8D, 0x4, 0x10)
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_57_5D0B end

    SaveToFile()

Try(main)
