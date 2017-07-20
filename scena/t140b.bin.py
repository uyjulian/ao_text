from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t140b.bin",                # FileName
        "t140b",                    # MapName
        "t140b",                    # Location
        0x00BB,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 187, 0, 0, 0, 1],
    )

    BuildStringList((
        "t140b",                  # 0
        "Keya",                 # 1
    ))

    AddCharChip((
        "chr/ch13600.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 2,   0.0,                   -75.0,                 2.0,                   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  25.0,                  -0.4000000059604645,   1.0])

    ChipFrameInfo(404, 0)                                        # 0

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_195",          # 01, 1
        "Function_2_1B4",          # 02, 2
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    Return()

    # Function_0_194 end

    def Function_1_195(): pass

    label("Function_1_195")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1AD")

    Sound(126, 1, 50, 0)
    Return()

    # Function_1_195 end

    def Function_2_1B4(): pass

    label("Function_2_1B4")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(852)
    SoundLoad(3616)
    SoundLoad(3617)
    SoundLoad(3618)
    SoundLoad(4109)
    SoundLoad(3330)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 0, 5000, -68000, 0)
    OP_90(0x102, -800, 5000, -69000, 0)
    OP_90(0x103, 900, 5000, -68800, 0)
    OP_90(0x104, 200, 5000, -70000, 0)
    OP_90(0x109, -1000, 5000, -71000, 0)
    OP_90(0x105, 1100, 5000, -71000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 0, 5000, -45000, 0)
    SetChrFlags(0x8, 0x4)
    PlayEffect(0x0, 0x0, 0x8, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopBGM(0xFA0)
    FadeToBright(1000, 0)
    OP_68(0, 4500, -57000, 0)
    OP_68(0, 3000, -57000, 3000)
    MoveCamera(0, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)

    def lambda_323():
        OP_9B(0x0, 0x101, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_323)
    Sleep(50)

    def lambda_33B():
        OP_9B(0x0, 0x102, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33B)
    Sleep(50)

    def lambda_353():
        OP_9B(0x0, 0x103, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_353)
    Sleep(50)

    def lambda_36B():
        OP_9B(0x0, 0x104, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_36B)
    Sleep(50)

    def lambda_383():
        OP_9B(0x0, 0x109, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_383)
    Sleep(50)

    def lambda_39B():
        OP_9B(0x0, 0x105, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_39B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00002F#6PThere she is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PT-thank goodness\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sound(852, 2, 60, 0)
    Fade(1000)
    OP_68(0, 1000, -45000, 0)
    MoveCamera(180, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(14000, 4000)
    OP_6F(0x79)
    OP_25(0x354, 0x28)
    Fade(1000)
    OP_68(0, 32000, -7500, 0)
    MoveCamera(0, -39, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(48400, 0)
    SetCameraDistance(47900, 3000)
    OP_6F(0x79)
    SetCameraDistance(46900, 20000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#05815F#3616V#60W#12P#NWhy…\x02\x03",
            "#3617V#60WWhy…\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE21)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(1, 180, -1, -1)

    AnonymousTalk(
        0x101,
        "#00007F#4SKeya#3330V……!\x02",
    )

    CloseMessageWindow()
    OP_24(0xD02)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_25(0x354, 0x3C)
    Fade(500)
    OP_90(0x101, -100, 5000, -58300, 0)
    OP_90(0x102, -1500, 5000, -57500, 0)
    OP_90(0x103, 1500, 5000, -57800, 0)
    OP_90(0x104, 200, 5000, -60100, 0)
    OP_90(0x109, -1000, 5000, -59800, 0)
    OP_90(0x105, 1200, 5000, -59900, 0)
    OP_68(0, 1100, -45000, 0)
    OP_68(0, 1100, -48800, 3500)
    MoveCamera(180, 22, 0, 0)
    MoveCamera(180, 12, 0, 3500)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)

    def lambda_62B():
        OP_9B(0x0, 0x101, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_62B)
    Sleep(50)

    def lambda_643():
        OP_9B(0x0, 0x102, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_643)
    Sleep(50)

    def lambda_65B():
        OP_9B(0x0, 0x103, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_65B)
    Sleep(50)

    def lambda_673():
        OP_9B(0x0, 0x104, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_673)
    Sleep(50)

    def lambda_68B():
        OP_9B(0x0, 0x109, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_68B)
    Sleep(50)

    def lambda_6A3():
        OP_9B(0x0, 0x105, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6A3)
    WaitChrThread(0x102, 0)

    def lambda_6BC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BC)
    WaitChrThread(0x103, 0)

    def lambda_6CD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6CD)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#5PKeA, are you ok?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PWas good……\x01",
            "I am not hurt! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#05815F#40W#5P….\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Fade(500)
    StopSound(852, 700, 60)
    StopEffect(0x0, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#05805F#3618V#6P#30Wthat~……?\x02\x03",
            "#05810F#4109VWhat's wrong Lloyd\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100D)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00006F#5PGaku~!\x02\x03",
            "#00011FWhat's wrong.. You know…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PKeA, why are you here\x02\x03",
            "#00200FFrom Lloyd's room\x01",
            "You are walking, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#05805F#6P#30W???\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(400)
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(400)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#05811F#6P#30WThis is.. The castle from before?\x02\x03",
            "#05805FWhy is KeA here?\x02",
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
        0x105,
        (
            "#10306F#5PWhew ……\x01",
            "It seems I do not remember at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PRight, sleeping like this\x01",
            "Did they come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PNo, I gotta do it,\x01",
            "It's too terrible and too sleepy ……\x02\x03",
            "#00301FKeA, you really don't remember anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#05803F#6P#30WHmmmm\x02\x03",
            "#05808F…… Kaoru in some sort of dream\x01",
            "It sounds like a calling voice ……\x02\x03",
            "#05805F…………that?\x01",
            "I wonder if Ka'a was calling …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#5PHmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PWhatching\x01",
            "A dream thing, it can not be helped.\x02\x03",
            "#00102FAnyway I'm just glad you're ok\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PRight\x02\x03",
            "#00002FOkay, we also\x01",
            "I will return to the hotel once.\x02\x03",
            "Ka'aa, back to the room\x01",
            "You are going to sleep properly?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    Sound(3659, 255, 80, 0)

    ChrTalk(
        0x8,
        "#05809F#6PRight!\x02",
    )

    CloseMessageWindow()
    OP_24(0xE4B)
    StopSound(126, 2000, 50)
    FadeToDark(1500, 0, -1)
    SetCameraDistance(15750, 1500)
    OP_6F(0x79)
    OP_0D()
    WaitBGM()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyds who returned to the hotel afterwards\x01",
            "After laying down Ka'aa\x01",
            "Contact the security department of Michelin … …\x02\x03",
            "Described the situation and went to the scene again\x01",
            "After all, no abnormality remained.\x02\x03",
            "And dawn __ - finally back to the hotel\x01",
            "After taking sleep until near noon ……\x02\x03",
            "Together with Maria Bell who came to pick me up\x01",
            "Lloyd's left Michelam.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ReplaceBGM(-1, -1)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1B4 end

    SaveToFile()

Try(main)
