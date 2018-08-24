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
        "Function_3_17DC",         # 03, 3
        "Function_4_1818",         # 04, 4
        "Function_5_1838",         # 05, 5
        "Function_6_185C",         # 06, 6
        "Function_7_1887",         # 07, 7
        "Function_8_18BF",         # 08, 8
        "Function_9_18F1",         # 09, 9
        "Function_10_1915",        # 0A, 10
        "Function_11_1939",        # 0B, 11
        "Function_12_1978",        # 0C, 12
        "Function_13_199C",        # 0D, 13
        "Function_14_19C7",        # 0E, 14
        "Function_15_19EB",        # 0F, 15
        "Function_16_1A1D",        # 10, 16
        "Function_17_1A84",        # 11, 17
        "Function_18_1AB6",        # 12, 18
        "Function_19_1B30",        # 13, 19
        "Function_20_1B5A",        # 14, 20
        "Function_21_1BEB",        # 15, 21
        "Function_22_1C7C",        # 16, 22
        "Function_23_1D0D",        # 17, 23
        "Function_24_1D51",        # 18, 24
        "Function_25_1D85",        # 19, 25
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
            "#12306F#11P#60W...............\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x101,
        "Voice",
        "#3336V#5P#N#40W#20A─Found you.\x02",
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
            "#12306F#3649V#11P#60W#30A...How... did you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#00000F#5P#30WBecause I heard your\x01",
            "voice.\x02\x03",
            "#00004FI've always been able...\x01",
            "to hear your voice, KeA.\x02\x03",
            "After I strained my ears\x01",
            "and felt it...\x02\x03",
            "#00002FI figured out where...\x01",
            "the voice of your heart\x01",
            "is, KeA.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12314F#11P#40WI see... Ehehe...\x02\x03",
            "#12308F...But KeA... has no\x01",
            "right to make Lloyd feel\x01",
            "like that...\x02\x03",
            "#12306FAfter all... After all\x01",
            "KeA...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P#30WKeA, that's not true.\x02\x03",
            "#00013FNo matter how you were\x01",
            "born─\x02",
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
            "#12311F#3650V#11P#4S#30W#20AIt is true!\x02",
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
            "#12307F#12P#40WKeA isn't a real human\x01",
            "and doesn't even have a\x01",
            "real heart and soul!\x02\x03",
            "I didn't have the right\x01",
            "to be treated kindly like\x01",
            "that, to be protected!\x02\x03",
            "#12311FAnd yet... And yet,\x01",
            "KeA...!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    def lambda_7CA():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7CA)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_7EA():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7EA)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00008F#5P#40W...............\x02",
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
            "#00002F#5P#30W─Listen, KeA.\x02\x03",
            "It's been more than half\x01",
            "a year since you came to\x01",
            "live with us...\x02\x03",
            "#00004FHow much happiness do\x01",
            "you think you've given\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#12P#40W...............\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00000F#5P#30WIt's probably the same\x01",
            "happiness you've felt,\x01",
            "or maybe even more.\x02\x03",
            "#00002FKeA... Wasn't it fun\x01",
            "being with us?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#12P#30WIt was! I was incredibly...\x01",
            "happy!\x02\x03",
            "#12311FBut that... That might only\x01",
            "be because KeA made you all\x01",
            "feel that way, Lloyd!\x02\x03",
            "It might only be because\x01",
            "KeA manipulated everyone's\x01",
            "precious hearts!\x02\x03",
            "#12316F#40WIt could be... It could\x01",
            "be...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_AC3():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AC3)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_AE3():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AE3)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00001F#5P#30W...............\x02",
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

    def lambda_B59():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B59)
    WaitChrThread(0x8, 2)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    BeginChrThread(0x101, 1, 0, 14)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30WYou see... I don't know what started\x01",
            "it.\x02\x03",
            "#00004FWe don't feel like we were manipulated,\x01",
            "and even if we had been, I think we\x01",
            "wouldn't have minded at all.\x02\x03",
            "#00000FKittens and human babies are\x01",
            "unconditionally lovely creatures you\x01",
            "just want to protect, right?\x02\x03",
            "Even that "power" you have, isn't it\x01",
            "something just like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12317F#12P#40W...Ah...\x02\x03",
            "...............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PAlso, we can't measure the\x01",
            "time we spent together\x01",
            "with such a "power".\x02",
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
            "#40W#3CPracticing cooking together,\x01",
            "sleeping and sleeping in\x01",
            "late in the same bed.\x02",
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
            "#40W#3CReading books with Elie and\x01",
            "hanging everyone's laundry\x01",
            "on the roof to dry.\x02",
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
            "#40W#3CCleaning with Tio and\x01",
            "buying Mishy's limited\x01",
            "edition merchandise.\x02",
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
            "#40W#3CPlaying poker with Randy\x01",
            "and going to shop at the\x01",
            "East Street stalls.\x02",
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
            "#40W#3CDoing laundry with chief\x01",
            "and napping with Zeit\x01",
            "and the others.\x02",
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
            "#00000F#5P─Do you really think all\x01",
            "of that has been a lie?\x02",
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
            "#12306F#12P#40W...It... wasn't a lie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5P#30WIn that case, that's our\x01",
            ""truth".\x02\x03",
            "#00004FAnd as long as there is\x01",
            "that "truth"...\x02\x03",
            "No matter what difficulties\x01",
            "are in store for us, we\x01",
            "won't ever lose.\x02\x03",
            "#00000FThat's why, KeA... You\x01",
            "needn't shoulder everything\x01",
            "by yourself.\x02\x03",
            "It'll be fine if we all do\x01",
            "our best, including you.\x02\x03",
            "#00009FThat's what you call\x01",
            ""friends"... And "family",\x01",
            "am I not right?\x02",
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
            "#12316F#3652V#50W#35ALloyd......\x01",
            "Lloooooyd...!\x02",
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
            "#05817F#3653V#12P#40W#70A...Oooh.... AAAAH...!\x02\x03",
            "#3654V#35A#4SWaaaaaaaah!\x02",
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
            "#00004FHaha... Nice tackle as\x01",
            "usual.\x02",
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
            "#00004F#5P#20A#30W─C'mon, let's head back.\x01",
            "Everyone's waiting for\x01",
            "us.\x02\x03",
            "#00002F#20AI'll keep holding you\x01",
            "like this, so grab on\x01",
            "tight, got it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#05818F#12P#20A#40WYeah... Yeah!\x02",
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

    def Function_3_17DC(): pass

    label("Function_3_17DC")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_17ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17ED)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
    CancelBlur(0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_3_17DC end

    def Function_4_1818(): pass

    label("Function_4_1818")

    Sleep(300)

    def lambda_1820():
        OP_A6(0xFE, 0x19, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1820)
    Sleep(500)
    Return()

    # Function_4_1818 end

    def Function_5_1838(): pass

    label("Function_5_1838")

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

    # Function_5_1838 end

    def Function_6_185C(): pass

    label("Function_6_185C")

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

    # Function_6_185C end

    def Function_7_1887(): pass

    label("Function_7_1887")

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

    # Function_7_1887 end

    def Function_8_18BF(): pass

    label("Function_8_18BF")

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

    # Function_8_18BF end

    def Function_9_18F1(): pass

    label("Function_9_18F1")

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

    # Function_9_18F1 end

    def Function_10_1915(): pass

    label("Function_10_1915")

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

    # Function_10_1915 end

    def Function_11_1939(): pass

    label("Function_11_1939")

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

    # Function_11_1939 end

    def Function_12_1978(): pass

    label("Function_12_1978")

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

    # Function_12_1978 end

    def Function_13_199C(): pass

    label("Function_13_199C")

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

    # Function_13_199C end

    def Function_14_19C7(): pass

    label("Function_14_19C7")

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

    # Function_14_19C7 end

    def Function_15_19EB(): pass

    label("Function_15_19EB")

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

    # Function_15_19EB end

    def Function_16_1A1D(): pass

    label("Function_16_1A1D")

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

    # Function_16_1A1D end

    def Function_17_1A84(): pass

    label("Function_17_1A84")

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

    # Function_17_1A84 end

    def Function_18_1AB6(): pass

    label("Function_18_1AB6")

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

    def lambda_1B0B():
        OP_A6(0xFE, 0x1E, 0x0, 0x3E8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B0B)
    SetChrSubChip(0xFE, 0x13)
    Sleep(50)
    Sound(811, 0, 80, 0)
    Sleep(325)
    Return()

    # Function_18_1AB6 end

    def Function_19_1B30(): pass

    label("Function_19_1B30")

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

    # Function_19_1B30 end

    def Function_20_1B5A(): pass

    label("Function_20_1B5A")

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

    # Function_20_1B5A end

    def Function_21_1BEB(): pass

    label("Function_21_1BEB")

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

    # Function_21_1BEB end

    def Function_22_1C7C(): pass

    label("Function_22_1C7C")

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

    # Function_22_1C7C end

    def Function_23_1D0D(): pass

    label("Function_23_1D0D")

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

    # Function_23_1D0D end

    def Function_24_1D51(): pass

    label("Function_24_1D51")

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

    # Function_24_1D51 end

    def Function_25_1D85(): pass

    label("Function_25_1D85")

    Sound(934, 0, 100, 0)
    Sleep(1000)
    Sound(222, 0, 50, 0)
    Sleep(500)
    Sound(928, 0, 100, 0)
    Return()

    # Function_25_1D85 end

    SaveToFile()

Try(main)
