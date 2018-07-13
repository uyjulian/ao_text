from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9014.bin",                # FileName
        "m9014",                    # MapName
        "m9014",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9014",                  # 0
        "KeA",                    # 1
        "KeA",                    # 2
        "SE制御",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(336, 0)                                        # 0

    ScpFunction((
        "Function_0_150",          # 00, 0
        "Function_1_160",          # 01, 1
        "Function_2_165",          # 02, 2
        "Function_3_182C",         # 03, 3
        "Function_4_1868",         # 04, 4
        "Function_5_1888",         # 05, 5
        "Function_6_18AC",         # 06, 6
        "Function_7_18D7",         # 07, 7
        "Function_8_190F",         # 08, 8
        "Function_9_1941",         # 09, 9
        "Function_10_1965",        # 0A, 10
        "Function_11_1989",        # 0B, 11
        "Function_12_19C8",        # 0C, 12
        "Function_13_19EC",        # 0D, 13
        "Function_14_1A17",        # 0E, 14
        "Function_15_1A3B",        # 0F, 15
        "Function_16_1A6D",        # 10, 16
        "Function_17_1AD4",        # 11, 17
        "Function_18_1B06",        # 12, 18
        "Function_19_1B80",        # 13, 19
        "Function_20_1BAA",        # 14, 20
        "Function_21_1C3B",        # 15, 21
        "Function_22_1CCC",        # 16, 22
        "Function_23_1D5D",        # 17, 23
        "Function_24_1DA1",        # 18, 24
        "Function_25_1DD5",        # 19, 25
    ))


    def Function_0_150(): pass

    label("Function_0_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_15F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_15F")

    Return()

    # Function_0_150 end

    def Function_1_160(): pass

    label("Function_1_160")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_160 end

    def Function_2_165(): pass

    label("Function_2_165")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10800.itc", 0x1E)
    LoadChrToIndex("chr/ch10801.itc", 0x1F)
    LoadChrToIndex("apl/ch51757.itc", 0x21)
    LoadChrToIndex("apl/ch51753.itc", 0x22)
    LoadChrToIndex("apl/ch51754.itc", 0x23)
    LoadEffect(0x0, "battle/cr036301.eff")
    SoundLoad(3336)
    SoundLoad(3649)
    SoundLoad(3650)
    SoundLoad(3651)
    SoundLoad(3652)
    SoundLoad(3653)
    SoundLoad(3654)
    SoundLoad(111)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    SetChrPos(0x101, -2250, 0, 2500, 135)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xD0, 0xD0, 0xD0, 0xFF, 0x0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 400, 0, 0, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 400, -500, 0, 180)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x1)
    SetMapObjFrame(0xFF, "point16_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break00_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break01_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break02_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break03_add", 0x2, "night")
    SetMapObjFrame(0xFF, "yuka00", 0x2, "night")
    SetMapObjFrame(0xFF, "point_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm02_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm03_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm04_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm05_add", 0x2, "night")
    OP_68(400, 850, 0, 0)
    MoveCamera(330, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(48000, 0)
    Sound(111, 2, 50, 0)
    FadeToBright(3000, 0)
    SetCameraDistance(38000, 9000)
    PlaceName2(340, 200, "c_plac69", 0x0, 3000)
    Sleep(6000)
    OP_A7(0x8, 0xE0, 0xE0, 0xE0, 0xFF, 0xBB8)
    OP_6F(0x79)
    Fade(1000)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#11P#60W............\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x101,
        "Voice",
        "#3336V#5P#N#40W#20A──Found you.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_68(-200, 850, 460, 2500)
    MoveCamera(330, 17, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(12800, 2500)
    BeginChrThread(0x101, 0, 0, 3)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#11P#60W#20A............\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#3649V#11P#60W#30A...How...did you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#00000F#5P#30WBecause I've heard your voice.\x02\x03",
            "#00004FI could always...\x01",
            "Hear your voice, KeA.\x02\x03",
            "After I strained my ears and felt it...\x02\x03",
            "#00002FI figured out where...\x01",
            "...The voice of your heart is, KeA.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12314F#11P#40WI see... Eheheh...\x02\x03",
            "#12308F...But KeA...\x01",
            "Has no right to make\x01",
            "Lloyd feel like that...\x02\x03",
            "#12306FAfter all...after all KeA...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P#30WKeA, that's not true.\x02\x03",
            "#00013FNo matter how you were born──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12311F#3650V#11P#4S#30W#20AIt's true!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(11500, 30000)
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#12P#40WKeA is not a real human and doesn't\x01",
            "even have a real heart and soul...!\x02\x03",
            "I didn't have the right to be treated\x01",
            "kindly like that, to be protected!\x02\x03",
            "#12311FAnd yet...\x01",
            "...And yet, KeA...!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    def lambda_7CC():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7CC)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_7EC():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7EC)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00008F#5P#40W............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x8, 0)
    SetCameraDistance(10400, 100000)
    PlayBGM("ed7581", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x245), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00002F#5P#30W──Listen, KeA.\x02\x03",
            "It's been more than half a year\x01",
            "since you came to stay with us...\x02\x03",
            "#00004FHow much happiness do\x01",
            "you think you've given us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#12P#40W............\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00000F#5P#30WI think maybe the same happiness\x01",
            "you've felt, or even more.\x02\x03",
            "#00002FKeA...\x01",
            "Wasn't it fun being with us?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#12P#30WIt was...!\x01",
            "I was incredibly...happy...!\x02\x03",
            "#12311FBut that...\x01",
            "That could be only because KeA \x01",
            "induced you all to feel that way, Lloyd!\x02\x03",
            "It could only be because KeA\x01",
            "manipulated everyone's precious hearts!\x02\x03",
            "#12316F#40WIt could be that...\x01",
            "...It could be that...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_AD4():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AD4)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_AF4():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AF4)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00001F#5P#30W............\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0)
    BeginChrThread(0x101, 1, 0, 10)
    WaitChrThread(0x101, 1)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00003F#5P#30WHey.\x02",
    )

    CloseMessageWindow()

    def lambda_B67():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B67)
    WaitChrThread(0x8, 2)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    BeginChrThread(0x101, 1, 0, 14)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30WYou see...\x01",
            "I don't know what started it.\x02\x03",
            "#00004FWe don't even feel like we were \x01",
            "manipulated, and even if we had been,\x01",
            "I think we wouldn't have minded at all.\x02\x03",
            "#00000FKittens and human babies are \x01",
            "unconditionally lovely creature\x01",
            "that you want to protect, right?\x02\x03",
            "Even that kind of "power" you have,\x01",
            "isn't it just something of that type?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12317F#12P#40W......oh......\x02\x03",
            "............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PAlso, we can't measure the time we\x01",
            "spent together with such a "power".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis311.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x101,
        (
            "#40W#3CPracticing cooking together, sleeping\x01",
            "and sleeping in late in the same bed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis386.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#40W#3CReading books together with Elie and\x01",
            "hanging everyone's laundry on the roof to dry.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis387.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#40W#3CCleaning together with Tio and buying\x01",
            "Michey's limited merchandise.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis388.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#40W#3CPlaying poker together with Randy and\x01",
            "going to shop in the stalls quarter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis389.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#40W#3CDoing the washing with Chief and\x01",
            "napping with Zeit and the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis390.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000F#5P──Do you really think that\x01",
            "all that has been a lie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#12P#40W...KeA thinks...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    BeginChrThread(0x8, 1, 0, 16)
    WaitChrThread(0x8, 1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#12P#40W...That...wasn't a lie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5P#30WIn that case, that's\x01",
            "the "truth" for us.\x02\x03",
            "#00004FAnd as long as there's that "truth"...\x02\x03",
            "No matter what difficulties will come\x01",
            "in the future, we won't ever lose.\x02\x03",
            "#00000FThat's why, KeA...\x01",
            "You don't need to shoulder everything by yourself.\x02\x03",
            "It'll be fine if we all do\x01",
            "our best, including you.\x02\x03",
            "#00009FThat's what you call "comrades"...\x01",
            "And "family", am I not right?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 15)
    WaitChrThread(0x101, 1)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12317F#3651V#12P#40W#30A...Llo...yd...\x02\x03",
            "#12316F#3652V#50W#35ALloyd......Loooooyd...!\x02",
        )
    )

    Sleep(3000)
    BeginChrThread(0x8, 1, 0, 17)
    WaitChrThread(0x8, 1)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0xA, 1, 0, 25)
    PlayEffect(0x0, 0xFF, 0x8, 0x41, 0, 350, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x10)
    Sleep(1000)
    OP_68(-400, 850, 400, 1000)
    MoveCamera(330, 17, 0, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(10000, 1000)
    BeginChrThread(0x8, 1, 0, 18)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#05817F#3653V#12P#40W#70A...uuuh....aaAAH...!\x02\x03",
            "#3654V#35A#4SWaaaaaaaah...!\x02",
        )
    )

    Sleep(8000)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00002F#5P#30W...KeA...\x02\x03",
            "#00004FHa ha...\x01",
            "Nice tackle as usual.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 19)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 1, 0, 20)
    BeginChrThread(0x8, 1, 0, 21)
    Sleep(1000)
    BeginChrThread(0xA, 1, 0, 24)
    SetMapObjFrame(0xFF, "point16_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break00_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break01_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break02_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break03_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "yuka00", 0x2, "to_d")
    SetMapObjFrame(0xFF, "point_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm02_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm03_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm04_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm05_add", 0x2, "to_d")
    Sleep(2500)

    ChrTalk(
        0x101,
        (
            "#00004F#5P#20A#30W──Come now, let's go back.\x01",
            "Everyone's waiting for us.\x02\x03",
            "#00002F#20AI'll keep holding you like this,\x01",
            "so grab on tight, got it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#05818F#12P#20A#40WYes...yes...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 22)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 1, 0, 23)
    Sleep(700)
    OP_68(0, 500, 0, 4000)
    MoveCamera(205, 13, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(11500, 4000)
    OP_6F(0x79)
    Sleep(1500)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    StopSound(111, 1000, 40)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("m9012", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_2_165 end

    def Function_3_182C(): pass

    label("Function_3_182C")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_183D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_183D)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
    CancelBlur(0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_3_182C end

    def Function_4_1868(): pass

    label("Function_4_1868")

    Sleep(300)

    def lambda_1870():
        OP_A6(0xFE, 0x19, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1870)
    Sleep(500)
    Return()

    # Function_4_1868 end

    def Function_5_1888(): pass

    label("Function_5_1888")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(111)
    SetChrSubChip(0xFE, 0x2)
    Sleep(111)
    SetChrSubChip(0xFE, 0x3)
    Sleep(333)
    Return()

    # Function_5_1888 end

    def Function_6_18AC(): pass

    label("Function_6_18AC")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(300)
    Return()

    # Function_6_18AC end

    def Function_7_18D7(): pass

    label("Function_7_18D7")

    OP_9B(0x0, 0xFE, 0xD, 0x6A4, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(200)
    Sound(812, 0, 60, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x14)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Fade(250)
    OP_0D()
    Return()

    # Function_7_18D7 end

    def Function_8_190F(): pass

    label("Function_8_190F")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Return()

    # Function_8_190F end

    def Function_9_1941(): pass

    label("Function_9_1941")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x1)
    Sleep(167)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Return()

    # Function_9_1941 end

    def Function_10_1965(): pass

    label("Function_10_1965")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0x6)
    Sleep(167)
    SetChrSubChip(0xFE, 0x7)
    Sleep(500)
    Return()

    # Function_10_1965 end

    def Function_11_1989(): pass

    label("Function_11_1989")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(571)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x8, 0x7)
    BeginChrThread(0x8, 1, 0, 12)
    SetChrSubChip(0xFE, 0xA)
    Sleep(429)
    WaitChrThread(0x8, 1)
    Return()

    # Function_11_1989 end

    def Function_12_19C8(): pass

    label("Function_12_19C8")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(429)
    Return()

    # Function_12_19C8 end

    def Function_13_19EC(): pass

    label("Function_13_19EC")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(571)
    Return()

    # Function_13_19EC end

    def Function_14_1A17(): pass

    label("Function_14_1A17")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_14_1A17 end

    def Function_15_1A3B(): pass

    label("Function_15_1A3B")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_15_1A3B end

    def Function_16_1A6D(): pass

    label("Function_16_1A6D")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Return()

    # Function_16_1A6D end

    def Function_17_1AD4(): pass

    label("Function_17_1AD4")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xA)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(125)
    SetChrSubChip(0xFE, 0x8)
    Sleep(500)
    Return()

    # Function_17_1AD4 end

    def Function_18_1B06(): pass

    label("Function_18_1B06")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x10)
    Sleep(125)
    SetChrSubChip(0xFE, 0x11)
    Sleep(125)
    SetChrSubChip(0xFE, 0x12)
    Sleep(125)
    SetChrFlags(0xFE, 0x20)
    OP_9D(0xFE, 0x96, 0x0, 0x0, 0x32, 0x3E8)
    ClearChrFlags(0xFE, 0x20)
    Sound(812, 0, 100, 0)

    def lambda_1B5B():
        OP_A6(0xFE, 0x1E, 0x0, 0x3E8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B5B)
    SetChrSubChip(0xFE, 0x13)
    Sleep(50)
    Sound(811, 0, 80, 0)
    Sleep(325)
    Return()

    # Function_18_1B06 end

    def Function_19_1B80(): pass

    label("Function_19_1B80")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 20, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(500)
    Return()

    # Function_19_1B80 end

    def Function_20_1BAA(): pass

    label("Function_20_1BAA")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Return()

    # Function_20_1BAA end

    def Function_21_1C3B(): pass

    label("Function_21_1C3B")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_21_1C3B end

    def Function_22_1CCC(): pass

    label("Function_22_1CCC")

    Fade(500)
    OP_68(-400, 950, 400, 800)
    SetCameraDistance(11000, 800)
    Sound(802, 0, 50, 0)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xF)
    SetChrFlags(0x8, 0x8)
    OP_0D()
    SetChrSubChip(0xFE, 0xF)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(500)
    SetChrSubChip(0xFE, 0x10)
    Sleep(167)
    SetChrSubChip(0xFE, 0x11)
    Sleep(167)
    SetChrSubChip(0xFE, 0x10)
    Sleep(167)
    SetChrSubChip(0xFE, 0xF)
    Sleep(833)
    Return()

    # Function_22_1CCC end

    def Function_23_1D5D(): pass

    label("Function_23_1D5D")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x1)
    Return()

    # Function_23_1D5D end

    def Function_24_1DA1(): pass

    label("Function_24_1DA1")

    Sleep(100)
    Sound(1022, 0, 100, 0)
    Sleep(3300)
    Sound(1022, 0, 100, 0)
    Sleep(3300)
    Sound(1022, 0, 100, 0)
    Sleep(3400)
    Sound(1022, 0, 100, 0)
    Sleep(1500)
    Sound(934, 0, 70, 0)
    Sound(1002, 0, 100, 0)
    Return()

    # Function_24_1DA1 end

    def Function_25_1DD5(): pass

    label("Function_25_1DD5")

    Sound(934, 0, 100, 0)
    Sleep(1000)
    Sound(222, 0, 50, 0)
    Sleep(500)
    Sound(928, 0, 100, 0)
    Return()

    # Function_25_1DD5 end

    SaveToFile()

Try(main)
