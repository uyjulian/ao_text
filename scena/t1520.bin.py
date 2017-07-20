from ScenarioHelper import *

def main():
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
        "Mallone",               # 1
        "Director Ashra",         # 2
        "Doctor Doctor",       # 3
        "Nurse machine",         # 4
        "Cecil",                 # 5
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
        "Function_8_59E",          # 08, 8
        "Function_9_662",          # 09, 9
        "Function_10_122F",        # 0A, 10
        "Function_11_1D96",        # 0B, 11
        "Function_12_1E85",        # 0C, 12
        "Function_13_1F92",        # 0D, 13
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
            "\"Introduction to cross-regional cuisine\" is available.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_59A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Braised stew\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_59A")

    TalkEnd(0xFF)
    Return()

    # Function_7_4ED end

    def Function_8_59E(): pass

    label("Function_8_59E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3")
    Call(0, 9)
    Jump("loc_65E")

    label("loc_5B3")


    ChrTalk(
        0xC,
        (
            "#01303FIf you know the truth of Mr. Guy's case,\x01",
            "I might as well proceed ….\x02\x03",
            "#01300FDo not push yourself.\x01",
            "You can live without anything\x01",
            "Because it is my best wishes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E")

    TalkEnd(0xFE)
    Return()

    # Function_8_59E end

    def Function_9_662(): pass

    label("Function_9_662")

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
            "#11P#01300F…… Ah, Lloyd's.\x02\x03",
            "Professor Seyland\x01",
            "Did work finish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, just a while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FIs Cecil on during a break?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01302FHuhu, I have a night duty today.\x01",
            "I was returning to preparations in various ways.\x02\x03",
            "#01304FFor sleepiness awake\x01",
            "Favorite tea\x01",
            "I thought that I should take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIt seems to be busy as usual … is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FTrue, take care of yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01309FHuhu, that's fine.\x01",
            "Looking like this I am tough.\x02\x03",
            "#01304F…… That kind of place is Mr. Guy\x01",
            "I wonder if there are also affected parts.\x02",
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
            "#6P#10105FBy the way, just a picture\x01",
            "It looked like I was watching it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FPerhaps,\x01",
            "Is that person in the picture so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01300FHuhu, would you like to take a look?\x02",
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
            "#00003FI wonder if this picture will be three years ago.\x02\x03",
            "#00002FIt is reflected on the right side\x01",
            "My brother, Guy Bannings.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        (
            "#10105FOk, this person ……\x02\x03",
            "#10102FHuhu, there is only Mr. Lloyd's brother\x01",
            "It is a very straight way.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00309FCecil is also quite beautiful! It is!\x02\x03",
            "#00306FCow, I also like Cecil's\x01",
            "I wanted to be a childhood friend …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00106FWell, Randy.\x02\x03",
            "#00102FBut when I look like this … …\x01",
            "One who really matches Cecil\x01",
            "I thought that it was.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xC,
        (
            "#01309FHehe, Thank you.\x01",
            "I will be happy if you say so.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            "#10302FHuff, and young Lloyd as well\x01",
            "You look cute.\x02\x03",
            "#10304FEven just looking at this picture,\x01",
            "Your demonic misleading pure women and children,\x01",
            "It feels like you can see its scales.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        "#00011F#4SWhat……! Is it?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x109,
        "#10106F(Yes, indeed … …)\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00111F(If it was a present time from that time,\x01",
            "It must be a pretty dangerous person … …)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#00006F…… somehow another strange label\x01",
            "I feel like being pasted.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xC,
        "#01309FHehu ……\x02",
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
            "#11P#01303F…… from when I took this picture\x01",
            "Various things have changed.\x02\x03",
            "#01308FFrom the day Guy died\x01",
            "What is not changed\x01",
            "It may be only me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FCecil elder sister …\x02\x03",
            "#00003FIt may take a while but …\x01",
            "Please wait.\x02\x03",
            "#00000FThe truth of my brother's case, certainly someday\x01",
            "Because I will grab it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, we also helped with that\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#01304F…, Huhu, thank you everyone.\x02\x03",
            "#01300FBut, do not push yourself.\x01",
            "You can live without anything\x01",
            "Because it is my best wishes.\x02\x03",
            "#01309FIf it gets carried into the hospital,\x01",
            "Asking Professor Seyland\x01",
            "Because I will prescribe Niga ~ Iio medicine?\x02",
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
            "#6P#00306FIf it was a medicine made by that female doctor\x01",
            "There seems to be a tremendous effect, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, even if you give out seriousness\x01",
            "It seems to be controlling freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FYou will be careful.\x02",
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

    # Function_9_662 end

    def Function_10_122F(): pass

    label("Function_10_122F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_136B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F7")

    ChrTalk(
        0x8,
        "Freshness, good news … ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Outpatient reception was restarted\x01",
            "Everyone in the hospital seems to be stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order for everyone to keep up,\x01",
            "I have to clean up and clean up more than usual!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1366")

    label("loc_12F7")


    ChrTalk(
        0x8,
        "Freshness, good news … ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order for everyone to keep up,\x01",
            "I have to clean up and clean up more than usual!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1366")

    Jump("loc_1D92")

    label("loc_136B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1414")

    ChrTalk(
        0x8,
        (
            "Recently, a trainee going out from the dormitory\x01",
            "I feel that the teachers' facial expressions are dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Patients in the hospital\x01",
            "Most of them can not come,\x01",
            "You should be worried after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_14B9")

    ChrTalk(
        0x8,
        (
            "Police and Mr. Tap\x01",
            "Dormitory cleaning and meal carry\x01",
            "Because I will help you, I am saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's been awkward, just staying in the hospital\x01",
            "I will be saved when I get a job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_14B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1545")

    ChrTalk(
        0x8,
        (
            "Now, Mr. Meifa\x01",
            "It seems that it is a holiday in the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone is working normally,\x01",
            "I want you to take a good rest on this aircraft.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1652")

    ChrTalk(
        0x8,
        (
            "In recent few days, many people\x01",
            "To the sympathy of the patient of the attack incident\x01",
            "It seems like I'm visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Especially the damage was great\x01",
            "Police and guard family members,\x01",
            "The expression is cloudy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In my case my family\x01",
            "After getting caught …… Agreeing that way,\x01",
            "I think my heart is torn apart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F6")

    label("loc_1652")


    ChrTalk(
        0x8,
        (
            "In recent few days, many people\x01",
            "To the sympathy of the patient of the attack incident\x01",
            "It seems like I'm visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In my case my family\x01",
            "After getting caught …… Agreeing that way,\x01",
            "I think my heart is torn apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F6")

    Jump("loc_1D92")

    label("loc_16FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_178C")

    ChrTalk(
        0x8,
        (
            "A train accident happened,\x01",
            "The teacher and resident doctors\x01",
            "They seem to be paying off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until now, to the best of my life\x01",
            "Let's say I have to clean it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1846")

    ChrTalk(
        0x8,
        (
            "According to the secretary's story,\x01",
            "It seems that it will rain tomorrow from morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anything, with a power net\x01",
            "The weather forecast can be seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, in a convenient world\x01",
            "That's what it was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18BA")

    label("loc_1846")


    ChrTalk(
        0x8,
        "It seems that it will rain tomorrow from morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Using the power net\x01",
            "To see the weather forecast,\x01",
            "It turned out to be a useful world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BA")

    Jump("loc_1D92")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CA")

    ChrTalk(
        0x8,
        (
            "Arios,\x01",
            "While my daughter is operating\x01",
            "It looked like I was restless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is told that it is \"the sword of the wind\"\x01",
            "Some people feel like people on the clouds\x01",
            "It will be many, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Looking ahead,\x01",
            "My daughter's feelings everywhere\x01",
            "I think I am a father.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A64")

    label("loc_19CA")


    ChrTalk(
        0x8,
        (
            "Arios,\x01",
            "While my daughter is operating\x01",
            "It looked like I was restless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Looking ahead,\x01",
            "My daughter's feelings everywhere\x01",
            "I think I am a father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A64")

    Jump("loc_1D92")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1AF2")

    ChrTalk(
        0x8,
        (
            "Today is unusual\x01",
            "Mr. Verdain seems to be off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently I do not have a break\x01",
            "It seems they were working,\x01",
            "I want you to take a good rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA4")

    ChrTalk(
        0x8,
        (
            "Freshness … ♪\x01",
            "This is a girls' dorm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Besides boys' dorms,\x01",
            "Feelings I have to clean carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…, Huhu, joke.\x01",
            "I'm serious about cleaning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C3E")

    label("loc_1BA4")


    ChrTalk(
        0x8,
        (
            "Oh, maybe ….\x01",
            "Ashura's chief director\x01",
            "I wonder if I'm oversleeping again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, yesterday as well.\x01",
            "It seems they were in the research building,\x01",
            "It might be a poor idea to wake it up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C3E")

    Jump("loc_1D92")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1C")

    ChrTalk(
        0x8,
        (
            "Freshness … ♪\x01",
            "O · · · · じ · fun ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, is there anyone else doing errands?\x01",
            "The men's dormitory is cleaning as you can see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are a teacher or a trainee,\x01",
            "Everyone is out.\x01",
            "Why do not you look for a ward?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D92")

    label("loc_1D1C")


    ChrTalk(
        0x8,
        (
            "Freshness … ♪\x01",
            "Yes, it was very beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On this terrace as it is,\x01",
            "I wonder if I will smoke delicious air.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D92")

    TalkEnd(0xFE)
    Return()

    # Function_10_122F end

    def Function_11_1D96(): pass

    label("Function_11_1D96")

    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1C")

    ChrTalk(
        0x9,
        (
            "…… Conducted by X-ray\x01",
            "I will examine every corner ~ ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… Supa … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FSounds like sleeping ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E6F")

    label("loc_1E1C")


    ChrTalk(
        0x9,
        (
            "…. Well,\x01",
            "Photosensitive quartz has run out … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… Supa … ….\x02",
    )

    CloseMessageWindow()

    label("loc_1E6F")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1D96 end

    def Function_12_1E85(): pass

    label("Function_12_1E85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F39")

    ChrTalk(
        0xA,
        (
            "From researchers\x01",
            "It is said that I am offending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, for a proper holiday\x01",
            "Several months have passed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am lucky, today I do my best\x01",
            "Let's have a rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F8E")

    label("loc_1F39")


    ChrTalk(
        0xA,
        "Physical condition management is definitely important.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a great holiday,\x01",
            "Let's have a rest today with full power.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8E")

    TalkEnd(0xFE)
    Return()

    # Function_12_1E85 end

    def Function_13_1F92(): pass

    label("Function_13_1F92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FA3")
    Jump("loc_2172")

    label("loc_1FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1FB1")
    Jump("loc_2172")

    label("loc_1FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1FBF")
    Jump("loc_2172")

    label("loc_1FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D6")

    ChrTalk(
        0xB,
        (
            "Because the outpatient is stopping,\x01",
            "Recently I have a holiday regularly\x01",
            "You got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's such a time but I am not happy obediently,\x01",
            "You can rest when you can rest\x01",
            "The chief has also told me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But, Shillon's guy\x01",
            "I am anxious just to leave it ……\x01",
            "I wonder if I will go see the state later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2172")

    label("loc_20D6")


    ChrTalk(
        0xB,
        (
            "Shiron 's guy …\x01",
            "While I am away I hesitate\x01",
            "You do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "… … Oh, stop it.\x01",
            "If you worry about Shillon\x01",
            "I do not feel distracted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2172")

    TalkEnd(0xFE)
    Return()

    # Function_13_1F92 end

    SaveToFile()

Try(main)
