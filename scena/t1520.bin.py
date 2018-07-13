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
        "Function_8_5B3",          # 08, 8
        "Function_9_683",          # 09, 9
        "Function_10_1358",        # 0A, 10
        "Function_11_21D6",        # 0B, 11
        "Function_12_22CC",        # 0C, 12
        "Function_13_2456",        # 0D, 13
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
            "The "Introduction To Crossbell Local Cuisine" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_5AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Boiled Stew"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5AF")

    TalkEnd(0xFF)
    Return()

    # Function_7_4ED end

    def Function_8_5B3(): pass

    label("Function_8_5B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C8")
    Call(0, 9)
    Jump("loc_67F")

    label("loc_5C8")


    ChrTalk(
        0xC,
        (
            "#01303FIf I knew the truth behind Guy's incident,\x01",
            "maybe I too could move forward, but...\x02\x03",
            "#01300FDon't do the impossible.\x01",
            "My greatest wish is that\x01",
            "you all can live uneventfully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67F")

    TalkEnd(0xFE)
    Return()

    # Function_8_5B3 end

    def Function_9_683(): pass

    label("Function_9_683")

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
            "#11P#01300F...Oh, it is Lloyd and friends.\x02\x03",
            "Did you finish Professor\x01",
            "Seiland's job, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, just now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FAre you on break, Miss Cecil?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01302FUh uh, because today I am on night duty,\x01",
            "I just came back to prepare some things.\x02\x03",
            "#01304FI was thinking to bring with me\x01",
            "my favourite black tea to keep\x01",
            "myself awake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FYou look busy as always...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FReally, be careful with your health.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01309FUh uh, I am fine.\x01",
            "I do not look like it, but I am tough.\x02\x03",
            "#01304F...I think that a part of this side\x01",
            "of me was influenced by Guy.\x02",
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
            "#6P#10105FNow that you mention him, it seems\x01",
            "you were looking at a photo just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FCould it be a\x01",
            "picture of him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01300FUh uh, do you want to see it?\x02",
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
            "#00003FI guess this picture is from three years ago?\x02\x03",
            "#00002FThe one on the right side is my\x01",
            "big brother, Guy Bannings.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10105FEeh, so this is him...\x02\x03",
            "#10102FUh uh, as expected from Mr. Lloyd's older\x01",
            "brother, he looks like a very upright person.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00309FMiss Cecil too is sooo beautiful!!\x02\x03",
            "#00306FKhhh, how I want to have been\x01",
            "Miss Cecil's childhood friend too...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00106F*sigh*, oh Randy.\x02\x03",
            "#00102FHowever, when I look at this...\x01",
            "I think he really was someone\x01",
            "who suited you, Miss Cecil.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xC,
        (
            "#01309FUh uh, thank you.\x01",
            "It makes me happy hearing you say this.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10302FUh uh, still, even the little Lloyd\x01",
            "has got quite the cute face, eh?\x02\x03",
            "#10304FJust by looking at this picture,\x01",
            "I feel like I can perceive a portion of that\x01",
            "charm that bewilders the pure women.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        "#00011F#4SHuuh...!?\x02",
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
            "back then, it's no wonder he's\x01",
            "quite the dangerous character...)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#00006F...Somehow I feel like a new\x01",
            "label was sticked to me.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xC,
        "#01309FUh uh...\x02",
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
            "#11P#01303FConsidering from when this picture was taken,\x01",
            "many things have ended up changing.\x02\x03",
            "#01308FAfter the day Guy passed away,\x01",
            "the only thing that didn't change...\x01",
            "Maybe it's me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FSister Cecil...\x02\x03",
            "#00003FMaybe it'll take some time, but...\x01",
            "Please wait.\x02\x03",
            "#00000FOne day I'll absolutely get to the\x01",
            "truth of big brother's incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, and we all too intend\x01",
            "to help you with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01304F...Uh uh, thank you, everyone.\x02\x03",
            "#01300FDon't do the impossible.\x01",
            "My greatest wish is that\x01",
            "you all can live uneventfully.\x02\x03",
            "#01309FIn case you will be carried into the hospital,\x01",
            "I will beg Professor Seiland to prescribe you\x01",
            "a biiitter medicine, you know?\x02",
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
            "#6P#00306FIf that female doctor made that, it seems\x01",
            "it would be extremely effective, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, it seems that if she went at it seriously\x01",
            "she could freely control even the bitterness.\x02",
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

    # Function_9_683 end

    def Function_10_1358(): pass

    label("Function_10_1358")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1458")

    ChrTalk(
        0x8,
        "Hum hum hum, hum hum hum...♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since the outpatients reception reopened,\x01",
            "it seems everyone in the hospital is in high spirits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since everyone is doing their best, I have\x01",
            "to give my all more than usual and clean!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14D5")

    label("loc_1458")


    ChrTalk(
        0x8,
        "Hum hum hum, hum hum hum...♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since everyone is doing their best, I have\x01",
            "to give my all more than usual and clean!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D5")

    Jump("loc_21D2")

    label("loc_14DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_15CC")

    ChrTalk(
        0x8,
        (
            "Lately, the facial expressions of the medical interns and\x01",
            "doctors coming and going from the dormitory look gloomy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Almost all the city patients who were\x01",
            "commuting to the hospital can't come...\x01",
            "That's really worrisome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D2")

    label("loc_15CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_169E")

    ChrTalk(
        0x8,
        (
            "It's a real help that Miss Polise and\x01",
            "Mr. Tap help out with the dormitory \x01",
            "cleanings and the meals delivery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they could get employed in the hospital\x01",
            "like that, it would me a lot too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D2")

    label("loc_169E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(
        0x8,
        (
            "It seems that Miss Meihua\x01",
            "is resting in her room now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone works non-stop on a regular basis,\x01",
            "so I wish they rest properly in these occasions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D2")

    label("loc_1749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AC")

    ChrTalk(
        0x8,
        (
            "It seems that in the last few days,\x01",
            "a lot of people came to visit the\x01",
            "raid incident patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The facial expressions of the members of\x01",
            "the police and CGF persons who were\x01",
            "injured very greatly are gloomy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What if my family had been caught\x01",
            "in that incident... When I think that,\x01",
            "it's like my heart is torn apart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_197F")

    label("loc_18AC")


    ChrTalk(
        0x8,
        (
            "It seems that in the last few days,\x01",
            "a lot of people came to visit the\x01",
            "raid incident patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What if my family had been caught\x01",
            "in that incident... When I think that,\x01",
            "it's like my heart is torn apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197F")

    Jump("loc_21D2")

    label("loc_1984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A4C")

    ChrTalk(
        0x8,
        (
            "It seems that all the doctors and\x01",
            "medical interns are out due to a\x01",
            "train derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that I have the chance, I'll clean\x01",
            "without leaving a single corner untouched.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D2")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B28")

    ChrTalk(
        0x8,
        (
            "According to the manager, tomorrow\x01",
            "it's going to rain from the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems he could see the weather\x01",
            "forecast on the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh*, the world has become\x01",
            "convenient, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BCD")

    label("loc_1B28")


    ChrTalk(
        0x8,
        "They say tomorrow it's going to rain from the morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Using the orbal net and being\x01",
            "able to see the weather forecast...\x01",
            "It has become a convenient world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCD")

    Jump("loc_21D2")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2D")

    ChrTalk(
        0x8,
        (
            "Mr. Arios hasn't been in a\x01",
            "calm state all the time while\x01",
            "his daughter was being operated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Being called the "Divine Blade of Wind",\x01",
            "there're many people who think of him \x01",
            "like he's a god-like person, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Seeing him like that, I thought he\x01",
            "was just like a normal father who\x01",
            "cares a lot for his daughter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DF4")

    label("loc_1D2D")


    ChrTalk(
        0x8,
        (
            "Mr. Arios hasn't been in a\x01",
            "calm state all the time while\x01",
            "his daughter was being operated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Seeing him like that, I thought he\x01",
            "was just like a normal father who\x01",
            "cares a lot for his daughter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF4")

    Jump("loc_21D2")

    label("loc_1DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1EA8")

    ChrTalk(
        0x8,
        (
            "Today it seems that doctor\x01",
            "Belldine is unusually on break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that recently he's\x01",
            "been working without resting,\x01",
            "so I hope he'll relax properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D2")

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_204A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F82")

    ChrTalk(
        0x8,
        (
            "Hum hum hum...♪\x01",
            "This is the female dormitory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I must clean it carefully, even\x01",
            "more than the male dormitory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Uh uh, I'm kidding.\x01",
            "I'm dead serious when it comes to cleaning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2045")

    label("loc_1F82")


    ChrTalk(
        0x8,
        (
            "Oh, could it be that...\x01",
            "Chief Ashram has\x01",
            "slept in again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhhm, it seems that yesterday too\x01",
            "she got to the research building late...\x01",
            "Even if she doesn't do it on purpose, it's pathetic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2045")

    Jump("loc_21D2")

    label("loc_204A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214E")

    ChrTalk(
        0x8,
        (
            "Hum hum hum...♪\x01",
            "Clean-ing-is-fuun☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Oh, do you have some business with anyone?\x01",
            "As you can see, I'm cleaning the male dormitory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The doctors and medical\x01",
            "interns are all out.\x01",
            "Why don't you look in the hospital ward?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21D2")

    label("loc_214E")


    ChrTalk(
        0x8,
        (
            "Hum hum hum...♪\x01",
            "Yes, it's become very clean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I guess I'll go out on the terrace now\x01",
            "and breath some delicious fresh air.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D2")

    TalkEnd(0xFE)
    Return()

    # Function_10_1358 end

    def Function_11_21D6(): pass

    label("Function_11_21D6")

    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226E")

    ChrTalk(
        0x9,
        (
            "...I'll look in every nook and cranny\x01",
            "with the orbal x-rays, you knooow♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...z....zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FS-Sleep talk...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22B6")

    label("loc_226E")


    ChrTalk(
        0x9,
        (
            "...Oh my my, the exposure\x01",
            "Quartz has broken...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...z....zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_22B6")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_21D6 end

    def Function_12_22CC(): pass

    label("Function_12_22CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CF")

    ChrTalk(
        0xA,
        (
            "I was told by the medical interns\x01",
            "to quit it already and get some rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that I think about it, how many months\x01",
            "has it been since I took a day off...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since it's a rare chance, today\x01",
            "I'm going to rest with all my might.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2452")

    label("loc_23CF")


    ChrTalk(
        0xA,
        "Keeping in good condition too is indeed important.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since it's a rare day off, today\x01",
            "I'm going to rest with all my might.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2452")

    TalkEnd(0xFE)
    Return()

    # Function_12_22CC end

    def Function_13_2456(): pass

    label("Function_13_2456")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2467")
    Jump("loc_2682")

    label("loc_2467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2475")
    Jump("loc_2682")

    label("loc_2475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2483")
    Jump("loc_2682")

    label("loc_2483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D9")

    ChrTalk(
        0xB,
        (
            "Because the outpatients flow has stopped,\x01",
            "recently I can take some occasional breaks.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Since the situation is like this I can't\x01",
            "be honestly happy, but I was told by\x01",
            "the Head Nurse to rest when I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, just leaving that Xilun\x01",
            "alone worries me...\x01",
            "I guess I'll go look at how she's doing later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2682")

    label("loc_25D9")


    ChrTalk(
        0xB,
        (
            "That Xilun...\x01",
            "She's not going to do something\x01",
            "bizarre while I'm not around, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...*sigh*, no, no.\x01",
            "If I'm worried about Xilun, I\x01",
            "won't be able to rest at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2682")

    TalkEnd(0xFE)
    Return()

    # Function_13_2456 end

    SaveToFile()

Try(main)
