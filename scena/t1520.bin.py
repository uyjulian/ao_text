from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1520.bin",                # FileName
        "t1520",                    # MapName
        "t1520",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 5, 0, 6],
    )

    BuildStringList((
        "t1520",                  # 0
        "Marona",                 # 1
        "Chief Ashram",           # 2
        "Doctor Belldine",        # 3
        "Nurse Meihua",           # 4
        "Cecil",                  # 5
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "apl/ch50146.itc",                   # 01
        "chr/ch29300.itc",                   # 02
        "chr/ch29800.itc",                   # 03
        "chr/ch05300.itc",                   # 04
    ))

    DeclNpc(4294962097, 0,       17700,   90,   261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(92529,   400,     49430,   315,  469,  0x0, 0,   1,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4294868457, 0,       53500,   180,  389,  0x0, 0,   2,   0,   0,   3,   0,   12,  255,  0)
    DeclNpc(204669,  0,       53000,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(154500,  0,       53400,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)

    DeclActor(95330,   0,       56250,   1200,    95330,   550,     56250,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(400, 0)                                        # 0

    ScpFunction((
        "Function_0_190",          # 00, 0
        "Function_1_240",          # 01, 1
        "Function_2_2A1",          # 02, 2
        "Function_3_302",          # 03, 3
        "Function_4_32D",          # 04, 4
        "Function_5_340",          # 05, 5
        "Function_6_49E",          # 06, 6
        "Function_7_4ED",          # 07, 7
        "Function_8_5AF",          # 08, 8
        "Function_9_672",          # 09, 9
        "Function_10_12C5",        # 0A, 10
        "Function_11_2090",        # 0B, 11
        "Function_12_2190",        # 0C, 12
        "Function_13_2315",        # 0D, 13
    ))


    def Function_0_190(): pass

    label("Function_0_190")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1C8"),
        (1, "loc_1D4"),
        (2, "loc_1E0"),
        (3, "loc_1EC"),
        (4, "loc_1F8"),
        (5, "loc_204"),
        (6, "loc_210"),
        (SWITCH_DEFAULT, "loc_21C"),
    )


    label("loc_1C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_204")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_210")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_228")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_23F")

    Return()

    # Function_0_190 end

    def Function_1_240(): pass

    label("Function_1_240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A0")
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -310, 0, 3650, 2000, 0x0)
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -14660, 0, 17700, 2000, 0x0)
    Jump("Function_1_240")

    label("loc_2A0")

    Return()

    # Function_1_240 end

    def Function_2_2A1(): pass

    label("Function_2_2A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_301")
    OP_95(0xFE, 79630, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 2680, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    Jump("Function_2_2A1")

    label("loc_301")

    Return()

    # Function_2_2A1 end

    def Function_3_302(): pass

    label("Function_3_302")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32C")
    OP_94(0xFE, 0xFFFE741A, 0xCD5A, 0xFFFE86D0, 0xD548, 0x3E8)
    Sleep(400)
    Jump("Function_3_302")

    label("loc_32C")

    Return()

    # Function_3_302 end

    def Function_4_32D(): pass

    label("Function_4_32D")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_4_32D end

    def Function_5_340(): pass

    label("Function_5_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_354")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_379")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_38D")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3B7")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_49D")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DC")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F0")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_415")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_429")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_442")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_49D")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47D")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 4)
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49D")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_49D")
    BeginChrThread(0x8, 0, 0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49D")
    ClearChrFlags(0xC, 0x80)

    label("loc_49D")

    Return()

    # Function_5_340 end

    def Function_6_49E(): pass

    label("Function_6_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4B0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4EC")

    Return()

    # Function_6_49E end

    def Function_7_4ED(): pass

    label("Function_7_4ED")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Introduction to\x01",
            "Crossbell's Local\x01",
            "Cuisine" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_5AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Boiled\x01",
            "Stew"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5AB")

    TalkEnd(0xFF)
    Return()

    # Function_7_4ED end

    def Function_8_5AF(): pass

    label("Function_8_5AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4")
    Call(0, 9)
    Jump("loc_66E")

    label("loc_5C4")


    ChrTalk(
        0xC,
        (
            "#01303FIf I knew the truth behind\x01",
            "Guy's case, I might be able\x01",
            "to move forward too, but...\x02\x03",
            "#01300FDon't overdo it. My\x01",
            "greatest wish is for you\x01",
            "all to live in peace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E")

    TalkEnd(0xFE)
    Return()

    # Function_8_5AF end

    def Function_9_672(): pass

    label("Function_9_672")

    EventBegin(0x0)
    Fade(500)
    OP_68(153430, 700, 53830, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20790, 0)
    SetChrPos(0x101, 153010, 0, 53370, 90)
    SetChrPos(0x102, 152340, 0, 54310, 90)
    SetChrPos(0x104, 151800, 0, 52830, 90)
    SetChrPos(0x109, 151060, 0, 54090, 90)
    SetChrPos(0x105, 150790, 0, 53090, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis000.itp")
    OP_4B(0xC, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#11P#01300F...My, it's Lloyd and\x01",
            "friends.\x02\x03",
            "Might you have finished\x01",
            "with Professor Seiland's\x01",
            "request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, we just did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FAre you on break, Cecil?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01302FHaha. I have the night shift\x01",
            "tonight. I was just getting some\x01",
            "things in order before heading back.\x02\x03",
            "#01304FI was thinking of bringing my\x01",
            "favorite black tea to keep myself\x01",
            "awake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FYou look busy as\x01",
            "always...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FTake care of yourself,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01309FHaha, it's all right.\x01",
            "I'm tougher than I look.\x02\x03",
            "#01304F...I wonder if Guy\x01",
            "influenced that side of\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10105FCome to think of it, it\x01",
            "seemed like you were looking\x01",
            "at a photo just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FCould he be the one in\x01",
            "the photo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01300FHaha. Want to see?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00003FThis was taken three\x01",
            "years ago, I guess.\x02\x03",
            "#00002FThe one on the right is\x01",
            "Guy Bannings, my big\x01",
            "brother.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10105FWow, so this is him...\x02\x03",
            "#10102FHaha. Maybe it's because of\x01",
            "your brother that you're such\x01",
            "a straight shooter, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00309FYou are so beautiful,\x01",
            "Cecil!!\x02\x03",
            "#00306FUgh. I want to have been\x01",
            "your childhood friend\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00106F*sigh*. Oh, Randy.\x02\x03",
            "#00102FBut, looking at you two together\x01",
            "like this... I think you really\x01",
            "were a good match for him, Cecil.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xC,
        (
            "#01309FHaha, thanks. I'm happy\x01",
            "to hear you say that.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10302FHaha. And you had a really cute\x01",
            "face when you were younger, didn't\x01",
            "you, Lloyd.\x02\x03",
            "#10304FJust looking at this picture, I\x01",
            "feel like I can see the part of you\x01",
            "that seduces pure-hearted girls.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        "#00011F#4SHuuuh...!?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        "#10106F(H-He's right...)\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00111F(If his current charm comes from\x01",
            "back then, it's certain that he's\x01",
            "quite the dangerous character...)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#00006F...I feel like I've been\x01",
            "labeled.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xC,
        "#01309FHaha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#11P#01303F...If you think about it, a\x01",
            "lot of things have changed\x01",
            "since this picture was taken.\x02\x03",
            "#01308FSince the day Guy passed\x01",
            "away, maybe I'm the only one\x01",
            "who hasn't changed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FCecil...\x02\x03",
            "#00003FIt may take quite some\x01",
            "time, but... Please wait\x01",
            "for me, Cecil.\x02\x03",
            "#00000FI swear I'll get to the\x01",
            "truth of my brother's\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRight. And we plan to\x01",
            "help him with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01304F...Haha. Thank you, everyone.\x02\x03",
            "#01300FBut, please don't force yourselves. After\x01",
            "all, my greatest wish is for you all to\x01",
            "live in peace.\x02\x03",
            "#01309FIn the event any of you are hospitalized,\x01",
            "I'll have Prof. Seiland prepare some\x01",
            "veeery bitter medicine for you, you hear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FIf she did make it, I'm\x01",
            "sure it'd be extremely\x01",
            "effective, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHaha. If she got serious,\x01",
            "I bet she could control\x01",
            "even the bitterness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FW-We'll be careful.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1CB, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 152510, 0, 53400, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_93(0xC, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_9_672 end

    def Function_10_12C5(): pass

    label("Function_10_12C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_143F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C3")

    ChrTalk(
        0x8,
        (
            "Hum hum hum, hum hum\x01",
            "hum...♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since the outpatient reception desk\x01",
            "reopened, it seems everyone in the\x01",
            "hospital is in high spirits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since everyone is doing their\x01",
            "best, I have work harder at\x01",
            "cleaning than usual!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_143A")

    label("loc_13C3")


    ChrTalk(
        0x8,
        (
            "Hum hum hum, hum hum\x01",
            "hum...♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since everyone is doing their\x01",
            "best, I have work harder at\x01",
            "cleaning than usual!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143A")

    Jump("loc_208C")

    label("loc_143F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1538")

    ChrTalk(
        0x8,
        (
            "The facial expressions of the interns and\x01",
            "doctors coming and going from the\x01",
            "dormitory have been looking gloomy lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Almost all the city outpatients who\x01",
            "were commuting to the hospital can't\x01",
            "come... That's really worrisome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_15F0")

    ChrTalk(
        0x8,
        (
            "It's a real help that Polise and\x01",
            "Tap help out with the dormitory\x01",
            "cleaning and the meal delivery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they were employed at\x01",
            "the hospital, it'd help\x01",
            "me a lot too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_15F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_16A6")

    ChrTalk(
        0x8,
        (
            "It seems that Meihua is\x01",
            "resting in her room now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone works around the clock on a\x01",
            "regular basis, so I hope they get\x01",
            "proper rest at the appropriate times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_16A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E6")

    ChrTalk(
        0x8,
        (
            "It seems that a lot of people\x01",
            "came to visit the attack\x01",
            "victims in the last few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The severely injured police\x01",
            "and CGF members have gloom\x01",
            "on their faces...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What if my family had been caught in the\x01",
            "attack... When I think about that, it\x01",
            "feels like my heart is being torn apart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18BD")

    label("loc_17E6")


    ChrTalk(
        0x8,
        (
            "It seems that a lot of people\x01",
            "came to visit the attack\x01",
            "victims in the last few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What if my family had been caught in the\x01",
            "attack... When I think about that, it\x01",
            "feels like my heart is being torn apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BD")

    Jump("loc_208C")

    label("loc_18C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1981")

    ChrTalk(
        0x8,
        (
            "It seems that all the doctors\x01",
            "and medical interns are out\x01",
            "due to a train derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that I have the chance,\x01",
            "I'll clean without leaving\x01",
            "a single corner untouched.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4A")

    ChrTalk(
        0x8,
        (
            "According to the\x01",
            "manager, it'll rain\x01",
            "tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems he saw the\x01",
            "weather forecast on the\x01",
            "orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh*, the world has\x01",
            "gotten so convenient,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ADB")

    label("loc_1A4A")


    ChrTalk(
        0x8,
        (
            "They say it's going to\x01",
            "rain tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Using the orbal net to see the\x01",
            "weather forecast... The world\x01",
            "has gotten more convenient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADB")

    Jump("loc_208C")

    label("loc_1AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C25")

    ChrTalk(
        0x8,
        (
            "Arios wasn't calm during the\x01",
            "entire time his daughter was\x01",
            "being operated on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Being called the Divine Blade of\x01",
            "Wind, there're many people who\x01",
            "think of him as godlike, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When I saw him like that, I thought\x01",
            "he was just like a normal father who\x01",
            "cares for his daughter an awful lot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CEA")

    label("loc_1C25")


    ChrTalk(
        0x8,
        (
            "Arios wasn't calm during the\x01",
            "entire time his daughter was\x01",
            "being operated on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When I saw him like that, I thought\x01",
            "he was just like a normal father who\x01",
            "cares for his daughter an awful lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEA")

    Jump("loc_208C")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D86")

    ChrTalk(
        0x8,
        (
            "I heard Dr. Belldine is\x01",
            "taking a rare vacation\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's been working without\x01",
            "rest recently, so I hope\x01",
            "he'll relax properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208C")

    label("loc_1D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E54")

    ChrTalk(
        0x8,
        (
            "Hum hum hum...♪ This is\x01",
            "the female dorm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I must clean it\x01",
            "carefully, even more\x01",
            "than the male one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Haha, I'm kidding.\x01",
            "I'm dead serious when it\x01",
            "comes to cleaning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F0A")

    label("loc_1E54")


    ChrTalk(
        0x8,
        (
            "Oh, could it be that...\x01",
            "Chief Ashram slept in\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, it seems she got to the research\x01",
            "building late yesterday... Even if she's\x01",
            "not doing it on purpose, it's pathetic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0A")

    Jump("loc_208C")

    label("loc_1F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_208C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2007")

    ChrTalk(
        0x8,
        (
            "Hum hum hum...♪ Clean-\x01",
            "ing-is-fuun☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Oh, do you have some business\x01",
            "with anyone? As you can see, I'm\x01",
            "cleaning the male dorm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The doctors and interns\x01",
            "are all out. Why don't you\x01",
            "look in the hospital ward?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_208C")

    label("loc_2007")


    ChrTalk(
        0x8,
        (
            "Hum hum hum...♪ Yes,\x01",
            "it's gotten very clean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I guess I'll go out on the\x01",
            "terrace now and breathe\x01",
            "some delicious fresh air.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208C")

    TalkEnd(0xFE)
    Return()

    # Function_10_12C5 end

    def Function_11_2090(): pass

    label("Function_11_2090")

    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2138")

    ChrTalk(
        0x9,
        (
            "...I'll look in every\x01",
            "nook and cranny with the\x01",
            "orbal x-rays, you knooow♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...z...zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-Is she talking in her\x01",
            "sleep...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_217A")

    label("loc_2138")


    ChrTalk(
        0x9,
        (
            "...Oh my my, the\x01",
            "exposure quartz broke...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...z...zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_217A")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_2090 end

    def Function_12_2190(): pass

    label("Function_12_2190")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2284")

    ChrTalk(
        0xA,
        (
            "I was told by the\x01",
            "interns to take a day\x01",
            "off already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Come to think of it, how\x01",
            "many months has it been\x01",
            "since I took a day off...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since I don't often take\x01",
            "vacations, I'm going to rest\x01",
            "today with all my might.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2311")

    label("loc_2284")


    ChrTalk(
        0xA,
        (
            "Maintenance of one's\x01",
            "health is certainly\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since I don't often take\x01",
            "vacations, I'm going to rest\x01",
            "today with all my might.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2311")

    TalkEnd(0xFE)
    Return()

    # Function_12_2190 end

    def Function_13_2315(): pass

    label("Function_13_2315")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2326")
    Jump("loc_253A")

    label("loc_2326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2334")
    Jump("loc_253A")

    label("loc_2334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2342")
    Jump("loc_253A")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_253A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2492")

    ChrTalk(
        0xB,
        (
            "Because the flow of outpatients\x01",
            "has stopped, I've been able to\x01",
            "take occasional breaks lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The situation being what it is, I'm\x01",
            "not happy about it, but the head\x01",
            "nurse told me to rest when I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But, it's leaving that Xilun alone\x01",
            "that worries me... I guess I'll go\x01",
            "see how she's doing later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_253A")

    label("loc_2492")


    ChrTalk(
        0xB,
        (
            "That Xilun... She's not going\x01",
            "to do something strange when\x01",
            "I'm not around, is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...*sigh*, no, no. If I\x01",
            "worry about Xilun, I won't\x01",
            "be able to rest at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253A")

    TalkEnd(0xFE)
    Return()

    # Function_13_2315 end

    SaveToFile()

Try(main)
