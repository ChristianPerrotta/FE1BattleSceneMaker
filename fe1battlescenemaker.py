import tkinter as tk
import os
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk, ImageDraw, ImageOps
import numpy as np
from fe1words import *

# ----------------------- MAIN UPDATE FUNCTION ----------------------- #
def UpdateImg(*args):
    if name_enemy.get() == 'Medeus':
        sprite_enemy.config(to = sprites['Medeus'])
        if int(sprite_enemy.get()) > 6:
            sprite_enemy.set(1)
    else:
        sprite_enemy.config(to = sprites[class_enemy.get()])
    base = Image.open(os.path.dirname(__file__)+r"\bg\bg1.png")
    base = DrawEnemySprite(base)
    base = DrawAllySprite(base)
    base = DrawEnemyHP(base)
    base = DrawAllyHP(base)
    base = WriteNames(base) #Names, levels, Classes, Weapons
    base = DrawHitAtkDef(base)
    #Battle Phase: Terrain
    if backtype.get() == 2:
        base = DrawTerrain(base)
    #Battle Phase: Enemy
    elif backtype.get() == 3:
        if enemy_action.get() == atk_msg[6]:
            sp_hpdmg_enemy.config(state='enabled')
            HP_or_DMG_enemy.config(text=' HP ')
        elif enemy_action.get() == atk_msg[12] or enemy_action.get() == atk_msg[1]:
            HP_or_DMG_enemy.config(text=' DMG')
            sp_hpdmg_enemy.config(state='enabled')
        else:
            sp_hpdmg_enemy.config(state='disabled')
        base = WriteEnemyPhase(base)
        #Write Final Message: Enemy
        if enemy_msg.get() == True:
            if (exp_box.get() == True
                and ch_exp_box.cget('state') == 'normal'
                and (drop_item.get() == True or (lv_up.get() == True and ch_lv_up.cget('state') == 'normal'))):
                    base = WriteExp(base)
            base = WriteFinalMsg(base)
    #Battle Phase: Ally
    elif backtype.get() == 4:
        if ally_action.get() == atk_msg[6]:
            sp_hpdmg_ally.config(state='enabled')
            HP_or_DMG_ally.config(text=' HP ')
        elif ally_action.get() == atk_msg[12] or ally_action.get() == atk_msg[1]:
            HP_or_DMG_ally.config(text=' DMG')
            sp_hpdmg_ally.config(state='enabled')
        else:
            sp_hpdmg_ally.config(state='disabled')
        base = WriteAllyPhase(base)
        #Write Final Message: Ally
        if ally_msg.get() == True:
            if (exp_box.get() == True
                and ch_exp_box.cget('state') == 'normal'
                and (drop_item.get() == True or (lv_up.get() == True and ch_lv_up.cget('state') == 'normal'))):
                    base = WriteExp(base)
            base = WriteFinalMsg(base)
    #DRAW EXP BOX OVER FINAL MESSAGE
    if (exp_box.get() == True
        and ch_exp_box.cget('state') == 'normal'
        and drop_item.get() == False
        and ((lv_up.get() == False and ch_lv_up.cget('state') == 'normal') or ch_lv_up.cget('state') == 'disabled')):
            base = WriteExp(base)
    global last_drawn
    global will_save
    last_drawn.paste(base)
    lb_image.config(image = last_drawn)
    if will_save == True:
        will_save = False
        save_path = '0'
        save_path = asksaveasfilename(defaultextension='.png', filetypes=[('png files', '*.png')],
                                      initialdir=os.path.dirname(__file__), title='Choose filename')
        try:
            base.save(save_path)
        except:
            pass

# ----------------------- WRITING FUNCTIONS ----------------------- #
def Write(list_: list, coord: tuple, b: Image, limit=0) -> Image:
    x = coord[0]
    y = coord[1]
    extra_line = 0
    characters = Image.open(os.path.dirname(__file__)+r"\bg\charactersJP.png")
    for sentence in list_:
        for i in allJP[sentence]:
            if limit != 0:
                if x >= (coord[0] + limit*8):
                    x = coord[0]
                    y = y + 16
                    extra_line += 1
            char_x = i[0]
            char_y = i[1]
            if i == TENTEN:
                char = characters.crop((char_x, char_y, char_x + 8, char_y + 3))
                b.paste(char, (x-8,y-3))
            elif i == MARU:
                char = characters.crop((char_x, char_y, char_x + 8, char_y + 4))
                b.paste(char, (x-8,y-4))
            else:
                char = characters.crop((char_x, char_y, char_x + 8, char_y + 8))
                b.paste(char, (x,y))
                x += 8
    if limit != 0:
        return b, extra_line
    else:
        return b

# ----------------------- REPLACE COLORS FUNCTION ----------------------- #

def ReplaceColor(orig: tuple, repl: tuple, img: Image) -> Image:
    img = img.convert('RGBA')
    data = np.array(img)
    data[(data == orig).all(axis = -1)] = repl
    img_replaced = Image.fromarray(data, mode='RGBA')
    return img_replaced

# ----------------------- INDIVIDUAL UPDATE FUNCTIONS ----------------------- #

def DrawEnemySprite(b):
    cl = class_enemy.get()
    sz = sprite_sizes[cl]
    sp_num = int(sprite_enemy.get()) - 1
    if name_enemy.get() == 'Medeus':
        sprite_sheet = Image.open(os.path.dirname(__file__)+r"\sprites\sp_medeus.png")
        cl = 'Medeus'
        sz = sprite_sizes[cl]
    elif name_enemy.get() == 'Maria':
        sprite_sheet = Image.open(os.path.dirname(__file__)+r"\sprites\sp_lena.png")
    else:
        sprite_sheet = Image.open(os.path.dirname(__file__)+r"\sprites\sp_" + cl.lower() + ".png")
    ht = sprite_sheet.height
    sp = sprite_sheet.crop((0 + sz*sp_num, 0, sz + sz*sp_num, ht))
    if name_enemy.get() != 'Medeus':
        sp = ImageOps.mirror(sp)
        if cl in ['Pegasus Knight', 'Paladin', 'Wyvern Knight']:
            sp = ReplaceColor(DARK_BLUE, PEGASUS_PINK, sp)
        else:
            sp = ReplaceColor(LIGHT_BLUE, LIGHT_PINK, sp)
            sp = ReplaceColor(DARK_BLUE, DARK_PINK, sp)
            sp = ReplaceColor(PURE_WHITE, PINK_WHITE, sp)
    x = int(sp_enemy_position_x.get())
    y = int(sp_enemy_position_y.get())
    b.paste(sp, ((CO_ENEMY_SPRITE[0] - (sz//2) + x), (CO_ENEMY_SPRITE[1] - ht - y)), sp.convert('RGBA'))
    return b

def DrawAllySprite(b):
    cl = class_ally.get()
    sz = sprite_sizes[cl]
    sp_num = int(sprite_ally.get()) - 1
    if name_ally.get() in ['Lena','Maria','Elice']:
        sprite_sheet = Image.open(os.path.dirname(__file__)+r"\sprites\sp_lena.png")
    elif name_ally.get() == 'Linde':
        sprite_sheet = Image.open(os.path.dirname(__file__)+r"\sprites\sp_linde.png")
    else:
        sprite_sheet = Image.open(os.path.dirname(__file__)+r"\sprites\sp_" + cl.lower() + ".png")
    ht = sprite_sheet.height
    sp = sprite_sheet.crop((0 + sz*sp_num, 0, sz + sz*sp_num, ht))
    x = int(sp_ally_position_x.get())
    y = int(sp_ally_position_y.get())
    b.paste(sp, ((CO_ALLY_SPRITE[0] - (sz//2) + x), (CO_ALLY_SPRITE[1] - ht - y)), sp.convert('RGBA'))
    return b

def DrawEnemyHP(b):
    draw = ImageDraw.Draw(b)
    hp = int(hp_enemy.get())
    hp_row2 = 0
    if hp > 26:
        hp_row2 = hp - 26
        hp = 26
    R = 255; G = 255; B = 255
    if hp_row2 > 0:
        for i in range(hp_row2):
            if (hp_row2 - int(dmg_enemy.get())) <= i:
                R = 0; G = 112; B = 236
            draw.rectangle(((CO_ENEMY_HP_BAR[0]+(i*4),CO_ENEMY_HP_BAR[1]-8),
                            (CO_ENEMY_HP_BAR[0]+2+(i*4),CO_ENEMY_HP_BAR[1]+5-8)), fill=(R,G,B))
    R = 255; G = 255; B = 255
    for i in range(hp):
        if (hp - (int(dmg_enemy.get()) - hp_row2)) <= i:
            R = 0; G = 112; B = 236
        draw.rectangle(((CO_ENEMY_HP_BAR[0]+(i*4),CO_ENEMY_HP_BAR[1]),
                        (CO_ENEMY_HP_BAR[0]+2+(i*4),CO_ENEMY_HP_BAR[1]+5)), fill=(R,G,B))
    return b

def DrawAllyHP(b):
    draw = ImageDraw.Draw(b)
    hp = int(hp_ally.get())
    hp_row2 = 0
    if hp > 26:
        hp_row2 = hp - 26
        hp = 26
    R = 255; G = 255; B = 255
    if hp_row2 > 0:
        for i in range(hp_row2):
            if (hp_row2 - int(dmg_ally.get())) <= i:
                R = 0; G = 112; B = 236
            draw.rectangle(((CO_ALLY_HP_BAR[0]+(i*4),CO_ALLY_HP_BAR[1]-8),
                            (CO_ALLY_HP_BAR[0]+2+(i*4),CO_ALLY_HP_BAR[1]+5-8)), fill=(R,G,B))
    R = 255; G = 255; B = 255
    for i in range(hp):
        if (hp - (int(dmg_ally.get()) - hp_row2)) <= i:
            R = 0; G = 112; B = 236
        draw.rectangle(((CO_ALLY_HP_BAR[0]+(i*4),CO_ALLY_HP_BAR[1]),
                        (CO_ALLY_HP_BAR[0]+2+(i*4),CO_ALLY_HP_BAR[1]+5)), fill=(R,G,B))
    return b

def WriteNames(b):
    #Enemy Name
    b = Write([name_enemy.get()], CO_ENEMY_NAME, b)
    #Ally Name
    b = Write([name_ally.get()], CO_ALLY_NAME, b)
    #Enemy Level
    lv = sp_level_enemy.get()
    b = Write(list(lv), CO_ENEMY_LV, b)
    #Ally Level
    lv = sp_level_ally.get()
    b = Write(list(lv), CO_ALLY_LV, b)
    #Enemy Class
    b = Write([class_enemy.get()], CO_ENEMY_CLASS, b)
    #Ally Class
    b = Write([class_ally.get()], CO_ALLY_CLASS, b)
    #Enemy Weapon
    b = Write([weapon_enemy.get()], CO_ENEMY_WEAPON, b)
    #Ally Weapon
    b = Write([weapon_ally.get()], CO_ALLY_WEAPON, b)
    return b

def DrawHitAtkDef(b):
    draw = ImageDraw.Draw(b)
    for i in range(int(hit_enemy.get())):
        draw.line((40 + i, 196, 40 + i, 196 + 3), fill = (76,220,72))
    for i in range(int(hit_ally.get())):
        draw.line((160 + i, 196, 160 + i, 196 + 3), fill = (76,220,72))
    for i in range(int(atk_enemy.get())):
        draw.line((40 + i, 204, 40 + i, 204 + 3), fill = (76,220,72))
    for i in range(int(atk_ally.get())):
        draw.line((160 + i, 204, 160 + i, 204 + 3), fill = (76,220,72))
    for i in range(int(def_enemy.get())):
        draw.line((40 + i, 212, 40 + i, 212 + 3), fill = (76,220,72))
    for i in range(int(def_ally.get())):
        draw.line((160 + i, 212, 160 + i, 212 + 3), fill = (76,220,72))
    return b

def DrawTerrain(b):
    #Terrain Box
    terrain = Image.open(os.path.dirname(__file__)+r"\bg\terrain_box_JP.png")
    b.paste(terrain, CO_TERRAIN)
    all_terrains = Image.open(os.path.dirname(__file__)+r"\bg\terrain_icons.png")
    #Enemy Terrain
    b = Write([enemy_terrain.get()], CO_ENEMY_TERRAIN, b)
    ID = terrains.index(enemy_terrain.get())
    terrain_icon_enemy = all_terrains.crop((0 + (ID*32),0,32 + (ID*32),32))
    b.paste(terrain_icon_enemy, CO_ENEMY_TERRAIN_ICON)
    avoid = str(terrains_avoid[enemy_terrain.get()])
    if len(avoid) == 2:
        b = Write(list(avoid), (64,168), b)
    else:
        b = Write(list(avoid), (72,168), b)
    #Ally Terrain
    b = Write([ally_terrain.get()], CO_ALLY_TERRAIN, b)
    ID = terrains.index(ally_terrain.get())
    terrain_icon_ally = all_terrains.crop((0 + (ID*32),0,32 + (ID*32),32))
    if ally_terrain.get() == 'Stadium':
        terrain_icon_ally = ImageOps.mirror(terrain_icon_ally)
    b.paste(terrain_icon_ally, CO_ALLY_TERRAIN_ICON)
    avoid = str(terrains_avoid[ally_terrain.get()])
    if len(avoid) == 2:
        b = Write(list(avoid), (192,168), b)
    else:
        b = Write(list(avoid), (200,168), b)
    return b

def WriteEnemyPhase(b):
    attackbox = Image.open(os.path.dirname(__file__)+r"\bg\attack_box.png")
    b.paste(attackbox, CO_ATK_BOX)
    if enemy_action.get() == '[DMG] damage!':
        b = Write(list(sp_hpdmg_enemy.get()) + [enemy_action.get()], CO_ATK_MSG, b)
    elif enemy_action.get() == '[UNIT] uses [MAGIC]':
        b = Write([name_enemy.get()] + ['wa '] + [weapon_enemy.get()] + [enemy_action.get()], CO_ATK_MSG, b)
    elif enemy_action.get() == "[UNIT]'s HP is restored by [HP]":
        b = Write([name_enemy.get()] + ['wa HP ga'] + list(sp_hpdmg_enemy.get()) + [enemy_action.get()], CO_ATK_MSG, b)
    elif enemy_action.get() == '[WPN] broke!':
        b = Write([weapon_enemy.get()] + [enemy_action.get()], CO_ATK_MSG, b)
    elif enemy_action.get() == 'Critical hit! [DMG] damage!':
        b = Write([enemy_action.get()] + list(sp_hpdmg_enemy.get()) + ['nodameejiwoataeta'], CO_ATK_MSG, b)
    elif enemy_action.get() == 'No damage!':
        b = Write([enemy_action.get()], CO_ATK_MSG, b)
    else:
        b = Write([name_enemy.get()] + [enemy_action.get()], CO_ATK_MSG, b)
    return b

def WriteAllyPhase(b):
    attackbox = Image.open(os.path.dirname(__file__)+r"\bg\attack_box.png")
    b.paste(attackbox, CO_ATK_BOX)
    if ally_action.get() == '[DMG] damage!':
        b = Write(list(sp_hpdmg_ally.get()) + [ally_action.get()], CO_ATK_MSG, b)
    elif ally_action.get() == '[UNIT] uses [MAGIC]':
        b = Write([name_ally.get()] + ['wa '] + [weapon_ally.get()] + [ally_action.get()], CO_ATK_MSG, b)
    elif ally_action.get() == "[UNIT]'s HP is restored by [HP]":
        b = Write([name_ally.get()] + ['wa HP ga'] + list(sp_hpdmg_ally.get()) + [ally_action.get()], CO_ATK_MSG, b)
    elif ally_action.get() == '[WPN] broke!':
        b = Write([weapon_ally.get()] + [ally_action.get()], CO_ATK_MSG, b)
    elif ally_action.get() == 'Critical hit! [DMG] damage!':
        b = Write([ally_action.get()] + list(sp_hpdmg_ally.get()) + ['nodameejiwoataeta'], CO_ATK_MSG, b)
    elif ally_action.get() == 'No damage!':
        b = Write([ally_action.get()], CO_ATK_MSG, b)
    else:
        b = Write([name_ally.get()] + [ally_action.get()], CO_ATK_MSG, b)
    return b

def WriteFinalMsg(b): #ONLY SHOWS 4 LINES AT ONCE
    #PASTES MESSAGE BOX ONTO MAIN IMAGE
    finalmsg = Image.open(os.path.dirname(__file__)+r"\bg\msg_box.png")
    b.paste(finalmsg, CO_MSG_BOX)
    #WRITES ALL THE TEXT ONTO THE BLACK SCREEN
    sc = Image.open(os.path.dirname(__file__)+r"\bg\text_box.png")
    extra = 0
    offset = 0
    excl = []
    #FIRST PART (THERE ARE 3 POSSIBILITIES)
    if final_message.get() in ["Withstood [ENEMY]'s attack!", '[ENEMY] was defeated!']:
        sc, extra = Write([name_enemy.get()] + [final_message.get()], (0,8), sc, 16)
        offset += extra + 1
        extra = 0
    elif final_message.get() == '[ALLY] collapsed!':
        sc, extra = Write([name_ally.get()] + [final_message.get()], (0,8), sc, 16)
        offset += extra + 1
        extra = 0
    else:
        sc, extra = Write([final_message.get()], (0,8), sc, 16)
        offset += extra + 1
        extra = 0
    #GAINED EXP
    if gain_exp.get() and (final_message.get() != '[ALLY] collapsed!'):
        if int(sp_exp_gained.get()) >= 20: excl = ['!!']
        sc, extra = Write([name_ally.get()] + ['wa '] + list(sp_exp_gained.get()) + ['[ALLY] earns [EXP] EXP!'] + excl,
                         (0, 8 + (offset)*16), sc, 16)
        offset += extra + 2
        extra = 0
    #ENEMY DROPPED WEAPON
    if drop_item.get() == True:
        sc, extra = Write([name_enemy.get()] + ['wa '] + [dropped.get()] + ['[ENEMY] was holding [ITEM]!'],
                          (0, 8 + (offset)*16), sc, 16)
        offset += extra + 1
        extra = 0
        sc, extra = Write([name_ally.get()] + ['wa '] + [dropped.get()] + ['[ALLY] obtained [ITEM].'],
                          (0, 8 + (offset)*16), sc, 16)
        offset += + extra + 1
        extra = 0
    #LEVELED UP
    if ch_lv_up.cget('state') == 'normal' and lv_up.get() == True:
        sc, extra = Write([name_ally.get()] + ['wa '], (0, 8+ (offset)*16), sc, 16)
        offset += extra + 1
        extra = 0
        sc, extra = Write(['level'] + list(str(int(sp_level_ally.get()) + 1)) + ['ninatta!'],
                          (0, 8+ (offset)*16), sc, 16)
        offset += extra + 1
        extra = 0
        if lv_str.get() == True:
            sc, extra = Write(['strength'] + ['ga 1agatta!'], (0, 8+ (offset)*16), sc, 16)
            offset += extra + 1
            extra = 0
        if lv_skl.get() == True:
            sc, extra = Write(['skill'] + ['ga 1agatta!'], (0, 8+ (offset)*16), sc, 16)
            offset += extra + 1
            extra = 0
        if lv_lck.get() == True:
            sc, extra = Write(['luck'] + ['ga 1agatta!'], (0, 8+ (offset)*16), sc, 16)
            offset += extra + 1
            extra = 0
        if lv_wpn.get() == True:
            sc, extra = Write(['weapon level'] + ['ga 1agatta!'], (0, 8+ (offset)*16), sc, 16)
            offset += extra + 1
            extra = 0
        if lv_spd.get() == True:
            sc, extra = Write(['speed'] + ['ga 1agatta!'], (0, 8+ (offset)*16), sc, 16)
            offset += extra + 1
            extra = 0
        if lv_hp.get() == True:
            sc, extra = Write(['max hp'] + ['ga 1agatta!'], (0, 8+ (offset)*16), sc, 16)
            offset += extra + 1
            extra = 0
    #PASTE A PORTION OF THE BLACK SCREEN ONTO THE MAIN IMAGE
    shown_text = sc.crop((0,0 + 16*(line - 1),128,64 + 16*(line - 1)))
    b.paste(shown_text, CO_FINAL_MSG_BLACK_SCREEN)
    return b

def LineDown():
    global line
    line = line + 1
    if line>=17: line = 16
    UpdateImg()

def LineUp():
    global line
    line = line - 1
    if line <=0: line = 1
    UpdateImg()

def WriteExp(b):
    expbox = Image.open(os.path.dirname(__file__)+r"\bg\exp_box.png")
    b.paste(expbox, CO_EXP_BOX)
    draw = ImageDraw.Draw(b)
    total_xp = int(sp_exp_current.get()) + int(sp_exp_gained.get())
    if total_xp >= 100:
        total_xp = total_xp - 100
    adjusted_xp = round(0.8*total_xp - 0.6)
    for i in range(adjusted_xp):
        draw.line((CO_EXP_BARS[0] + i, CO_EXP_BARS[1], CO_EXP_BARS[0] + i, CO_EXP_BARS[1] + 3), fill = (76,220,72))
    return b

def SaveImage():
    global will_save
    will_save = True
    UpdateImg()

# ----------------------- WIDGET DISPLAY FUNCTIONS ----------------------- #

def ChangeAllyDmg():
    if int(hp_ally.get()) <= int(dmg_ally.get()):
        dmg_ally.set(int(hp_ally.get()))
    dmg_ally.config(to = int(hp_ally.get()))
    UpdateImg()

def ChangeEnemyDmg():
    if int(hp_enemy.get()) <= int(dmg_enemy.get()):
        dmg_enemy.set(int(hp_enemy.get()))
    dmg_enemy.config(to = int(hp_enemy.get()))
    UpdateImg()

def SetAllySprites(s):
    sprite_ally.set(1)
    sprite_ally.config(to = sprites[s])
    om_name_ally.set_menu(ally_units[class_ally.get()][0], *ally_units[class_ally.get()])
    if class_ally.get() in sword_classes:
        om_weapon_ally.set_menu(swords[0], *(swords + ['None']))
    elif class_ally.get() in sword_and_lance_classes:
        om_weapon_ally.set_menu((swords+lances)[0], *(swords+lances + ['None']))
    elif class_ally.get() in axe_classes:
        om_weapon_ally.set_menu(axes[0], *(axes + ['None']))
    elif class_ally.get() in bow_classes:
        om_weapon_ally.set_menu(bows[0], *(bows + ['None']))
    elif class_ally.get() in dragon_classes:
        om_weapon_ally.set_menu(dragonstones[0], *(dragonstones + ['None']))
    elif class_ally.get() == 'Ballistician':
        om_weapon_ally.set_menu(ballistae[0], *(ballistae + ['None']))
    elif class_ally.get() == 'Mage':
        om_weapon_ally.set_menu(tomes[0], *(tomes + ['None']))
    elif class_ally.get() == 'Curate':
        om_weapon_ally.set_menu(staves[0], *(staves + ['None']))
    elif class_ally.get() == 'Bishop':
        om_weapon_ally.set_menu((tomes + staves)[0], *(tomes+staves + ['None']))
    UpdateImg()

def SetEnemySprites(s):
    sprite_enemy.set(1)
    sprite_enemy.config(to = sprites[s])
    om_name_enemy.set_menu(enemy_units[class_enemy.get()][0], *enemy_units[class_enemy.get()])
    if class_enemy.get() in sword_classes:
        om_weapon_enemy.set_menu(swords[0], *(swords + ['None']))
    elif class_enemy.get() in sword_and_lance_classes:
        om_weapon_enemy.set_menu((swords+lances)[0], *(swords+lances + ['None']))
    elif class_enemy.get() in axe_classes:
        om_weapon_enemy.set_menu(axes[0], *(axes + ['None']))
    elif class_enemy.get() in bow_classes:
        om_weapon_enemy.set_menu(bows[0], *(bows + ['None']))
    elif class_enemy.get() in dragon_classes:
        om_weapon_enemy.set_menu(dragonstones[0], *(dragonstones + ['None']))
    elif class_enemy.get() == 'Ballistician':
        om_weapon_enemy.set_menu(ballistae[0], *(ballistae + ['None']))
    elif class_enemy.get() == 'Mage':
        om_weapon_enemy.set_menu(tomes[0], *(tomes + ['None']))
    elif class_enemy.get() == 'Curate':
        om_weapon_enemy.set_menu(staves[0], *(staves + ['None']))
    elif class_enemy.get() == 'Bishop':
        om_weapon_enemy.set_menu((tomes+staves)[0], *(tomes+staves + ['None']))
    UpdateImg()

def DisableWidgets(*args):
    om_ally_terrain.config(state='disabled'); om_enemy_terrain.config(state='disabled')
    om_enemy_action.config(state='disabled'); ch_enemy_msg.config(state='disabled')
    om_ally_action.config(state='disabled');  ch_ally_msg.config(state='disabled')
    om_final_message.config(state='disabled'); ch_gain_exp.config(state = 'disabled')
    sp_exp_gained.config(state='disabled'); sp_exp_current.config(state='disabled')
    ch_drop_item.config(state='disabled'); menubutton.config(state='disabled')
    ch_lv_up.config(state='disabled'); ch_lv_str.config(state='disabled'); ch_lv_skl.config(state='disabled')
    ch_lv_lck.config(state='disabled'); ch_lv_wpn.config(state='disabled'); ch_lv_spd.config(state='disabled')
    ch_lv_hp.config(state='disabled')
    ch_exp_box.config(state='disabled')
    if backtype.get() == 2:
        om_ally_terrain.config(state='normal')
        om_enemy_terrain.config(state='normal')
    elif backtype.get() == 3 or backtype.get() == 4:
        if backtype.get() == 3:
            om_enemy_action.config(state='normal')
            ch_enemy_msg.config(state='normal')
        else:
            om_ally_action.config(state='normal')
            ch_ally_msg.config(state='normal') 
        if enemy_msg.get() == True or ally_msg.get() == True:
            om_final_message.config(state='normal')
            ch_drop_item.config(state='normal')
            if final_message.get() != '[ALLY] collapsed!':
                ch_gain_exp.config(state = 'normal')
                if gain_exp.get() == True:
                    sp_exp_gained.config(state='normal')
                    sp_exp_current.config(state='normal')
                    ch_exp_box.config(state='normal')
                    if int(sp_exp_current.get()) + int(sp_exp_gained.get()) >= 100:
                        ch_lv_up.config(state='normal')
                        if lv_up.get() == True:
                            ch_lv_str.config(state='normal')
                            ch_lv_skl.config(state='normal')
                            ch_lv_lck.config(state='normal')
                            ch_lv_wpn.config(state='normal')
                            ch_lv_spd.config(state='normal')
                            ch_lv_hp.config(state='normal')
            if drop_item.get() == True:
                menubutton.config(state='normal')
    UpdateImg()

# ----------------------- ROOT WINDOW ----------------------- #

root = tk.Tk()
root.title('FE1 Battle Scene Maker')
root.geometry('850x720')
root.resizable(False, False)

# ----------------------- FRAME: LEFT SIDE ----------------------- #

fr_left_side = tk.Frame(root, borderwidth=2, relief='groove')
#HEADER
lb_enemy = tk.Label(fr_left_side, text='Enemy Unit')
lb_ally = tk.Label(fr_left_side, text='Ally Unit')
#ENEMY NAME
lb_name = tk.Label(fr_left_side, text='Name')
name_enemy = tk.StringVar()
om_name_enemy = ttk.OptionMenu(fr_left_side, name_enemy, enemy_units['Mercenary'][0],
                               *enemy_units['Mercenary'], command=UpdateImg)
om_name_enemy.config(width=13)
#ALLY NAME
name_ally = tk.StringVar()
om_name_ally = ttk.OptionMenu(fr_left_side, name_ally, ally_units['Lord'][0],
                              *ally_units['Lord'], command=UpdateImg)
om_name_ally.config(width=13)
#ENEMY LEVEL
lb_level = tk.Label(fr_left_side, text='Level')
sp_level_enemy = ttk.Spinbox(fr_left_side, width=5, from_=1, to=20, command = UpdateImg)
sp_level_enemy.set(1)
#ALLY LEVEL
sp_level_ally = ttk.Spinbox(fr_left_side, width=5, from_=1, to=20, command = UpdateImg)
sp_level_ally.set(1)
#ENEMY CLASS
lb_class = tk.Label(fr_left_side, text='Class')
class_enemy = tk.StringVar()
om_class_enemy = ttk.OptionMenu(fr_left_side, class_enemy, en_classes[0], *en_classes, command=SetEnemySprites)
om_class_enemy.config(width=13)
#ALLY CLASS
class_ally = tk.StringVar()
om_class_ally = ttk.OptionMenu(fr_left_side, class_ally, classes[0], *classes, command=SetAllySprites)
om_class_ally.config(width=13)
#ENEMY WEAPON
lb_weapon = tk.Label(fr_left_side, text='Weapon')
weapon_enemy = tk.StringVar()
om_weapon_enemy = ttk.OptionMenu(fr_left_side, weapon_enemy, swords[0], *(swords + ['None']), command=UpdateImg)
om_weapon_enemy.config(width=13)
#ALLY WEAPON
weapon_ally = tk.StringVar()
om_weapon_ally = ttk.OptionMenu(fr_left_side, weapon_ally, swords[0], *(swords + ['None']), command=UpdateImg)
om_weapon_ally.config(width=13)
#SPRITES
lb_sprite = tk.Label(fr_left_side, text='Sprite')
sprite_enemy = ttk.Spinbox(fr_left_side, width=5, from_=1, to=9, command=UpdateImg)
sprite_enemy.set(1)
sprite_ally = ttk.Spinbox(fr_left_side, width=5, from_=1, to=15, command=UpdateImg)
sprite_ally.set(1)
#POSITIONS
lb_positions = tk.Label(fr_left_side, text='Positions')
#--------SUB-FRAME: ENEMY SPRITE POSITIONS
fr_enemy_sprite_positions = tk.Frame(fr_left_side)
sp_enemy_position_x = ttk.Spinbox(fr_enemy_sprite_positions, width = 5, from_=-100, to=100, command=UpdateImg)
sp_enemy_position_x.set(0)
sp_enemy_position_y = ttk.Spinbox(fr_enemy_sprite_positions, width = 5, from_=0, to=100, command=UpdateImg)
sp_enemy_position_y.set(0)

sp_enemy_position_x.grid(row=0, column=0)
sp_enemy_position_y.grid(row=0, column=1)
#--------SUB-FRAME: ALLY SPRITE POSITIONS
fr_ally_sprite_positions = tk.Frame(fr_left_side)
sp_ally_position_x = ttk.Spinbox(fr_ally_sprite_positions, width = 5, from_=-100, to=100, command=UpdateImg)
sp_ally_position_x.set(0)
sp_ally_position_y = ttk.Spinbox(fr_ally_sprite_positions, width = 5, from_=0, to=100, command=UpdateImg)
sp_ally_position_y.set(0)

sp_ally_position_x.grid(row=0, column=0)
sp_ally_position_y.grid(row=0, column=1)
#MAX HP
lb_max_hp = tk.Label(fr_left_side, text='Max HP')
hp_enemy = ttk.Spinbox(fr_left_side, width=5, from_=1, to=52, command = ChangeEnemyDmg)
hp_enemy.set(1)
hp_ally = ttk.Spinbox(fr_left_side, width=5, from_=1, to=52, command = ChangeAllyDmg)
hp_ally.set(1)
#DAMAGE
lb_damage = tk.Label(fr_left_side, text='Damage')
dmg_enemy = ttk.Spinbox(fr_left_side, width=5, from_=0, to=1, command = UpdateImg)
dmg_enemy.set(0)
dmg_ally = ttk.Spinbox(fr_left_side, width=5, from_=0, to=1, command = UpdateImg)
dmg_ally.set(0)
#HIT
lb_hit = tk.Label(fr_left_side, text='Hit')
hit_enemy = ttk.Spinbox(fr_left_side, width=5, from_=0, to=80, command = UpdateImg)
hit_enemy.set(0)
hit_ally = ttk.Spinbox(fr_left_side, width=5, from_=0, to=80, command = UpdateImg)
hit_ally.set(0)
#ATTACK
lb_atk = tk.Label(fr_left_side, text='Attack')
atk_enemy = ttk.Spinbox(fr_left_side, width=5, from_=0, to=80, command = UpdateImg)
atk_enemy.set(0)
atk_ally = ttk.Spinbox(fr_left_side, width=5, from_=0, to=80, command = UpdateImg)
atk_ally.set(0)
#DEFENSE
lb_def = tk.Label(fr_left_side, text='Defense')
def_enemy = ttk.Spinbox(fr_left_side, width=5, from_=0, to=80, command = UpdateImg)
def_enemy.set(0)
def_ally = ttk.Spinbox(fr_left_side, width=5, from_=0, to=80, command = UpdateImg)
def_ally.set(0)
#BATTLE PHASE
lb_battle_phase = tk.Label(fr_left_side, text='Battle Phase')
#RADIO BUTTONS FOR BATTLE
backtype = tk.IntVar(fr_left_side, 1)
enemy_msg = tk.BooleanVar()
ally_msg = tk.BooleanVar()

radio_initial = tk.Radiobutton(fr_left_side, text='Initial', variable = backtype, value=1, command=DisableWidgets)
radio_terrain = tk.Radiobutton(fr_left_side, text='Terrain', variable = backtype, value=2, command=DisableWidgets)
radio_enemy_action = tk.Radiobutton(fr_left_side, text='Enemy', variable = backtype, value=3, command=DisableWidgets)
ch_enemy_msg = tk.Checkbutton(fr_left_side, text='Message', variable = enemy_msg, state = 'disabled', command=DisableWidgets)
radio_ally_action = tk.Radiobutton(fr_left_side, text='Ally', variable = backtype, value=4, command=DisableWidgets)
ch_ally_msg = tk.Checkbutton(fr_left_side, text='Message', variable = ally_msg, state = 'disabled', command=DisableWidgets)

#Enemy Terrain
enemy_terrain = tk.StringVar()
om_enemy_terrain = ttk.OptionMenu(fr_left_side, enemy_terrain, terrains[0], *terrains, command=UpdateImg)
om_enemy_terrain.config(width=10, state='disabled')

#Ally Terrain
ally_terrain = tk.StringVar()
om_ally_terrain = ttk.OptionMenu(fr_left_side, ally_terrain, terrains[0], *terrains, command=UpdateImg)
om_ally_terrain.config(width=10, state='disabled')

#Enemy Action
enemy_action = tk.StringVar()
om_enemy_action = ttk.OptionMenu(fr_left_side, enemy_action, atk_msg[0], *atk_msg, command=UpdateImg)
om_enemy_action.config(width=10, state='disabled')

hp_dmg_enemy = tk.Frame(fr_left_side)
HP_or_DMG_enemy = tk.Label(hp_dmg_enemy, text=' HP ')
sp_hpdmg_enemy = ttk.Spinbox(hp_dmg_enemy, width=5, from_=1, to=99, command = UpdateImg)
sp_hpdmg_enemy.set(1)
sp_hpdmg_enemy.config(state='disabled')

HP_or_DMG_enemy.grid(row=0, column=0)
sp_hpdmg_enemy.grid(row=0, column=1)

#Ally Action
ally_action = tk.StringVar()
om_ally_action = ttk.OptionMenu(fr_left_side, ally_action, atk_msg[0], *atk_msg, command=UpdateImg)
om_ally_action.config(width=10, state='disabled')

hp_dmg_ally = tk.Frame(fr_left_side)
HP_or_DMG_ally = tk.Label(hp_dmg_ally, text=' HP ')
sp_hpdmg_ally = ttk.Spinbox(hp_dmg_ally, width=5, from_=1, to=99, command = UpdateImg)
sp_hpdmg_ally.set(1)
sp_hpdmg_ally.config(state='disabled')

HP_or_DMG_ally.grid(row=0, column=0)
sp_hpdmg_ally.grid(row=0, column=1)
# ----------------------- GRIDDING: LEFT SIDE ----------------------- #
PAD = 5
#HEADER
lb_enemy.grid(row=0, column=1, padx=PAD, pady=PAD)
lb_ally.grid(row=0, column=2, padx=PAD, pady=PAD)
#Names
lb_name.grid(row=1, column=0, padx=PAD, pady=PAD)
om_name_enemy.grid(row=1, column=1, padx=PAD, pady=PAD)
om_name_ally.grid(row=1, column=2, padx=PAD, pady=PAD)
#Levels
lb_level.grid(row=2, column=0, padx=PAD, pady=PAD)
sp_level_enemy.grid(row=2, column=1, padx=PAD, pady=PAD)
sp_level_ally.grid(row=2, column=2, padx=PAD, pady=PAD)
#Classes
lb_class.grid(row=3, column=0, padx=PAD, pady=PAD)
om_class_enemy.grid(row=3, column=1, padx=PAD, pady=PAD)
om_class_ally.grid(row=3, column=2, padx=PAD, pady=PAD)
#Sprites
lb_sprite.grid(row=4, column=0, padx=PAD, pady=PAD)
sprite_enemy.grid(row=4, column=1, padx=PAD, pady=PAD)
sprite_ally.grid(row=4, column=2, padx=PAD, pady=PAD)
#Positions
lb_positions.grid(row=5, column=0, padx=PAD, pady=PAD)
fr_enemy_sprite_positions.grid(row=5, column=1, padx=PAD, pady=PAD)
fr_ally_sprite_positions.grid(row=5, column=2, padx=PAD, pady=PAD)
#Weapons
lb_weapon.grid(row=6, column=0, padx=PAD, pady=PAD)
om_weapon_enemy.grid(row=6, column=1, padx=PAD, pady=PAD)
om_weapon_ally.grid(row=6, column=2, padx=PAD, pady=PAD)
#Max HP
lb_max_hp.grid(row=7, column=0, padx=PAD, pady=PAD)
hp_enemy.grid(row=7, column=1, padx=PAD, pady=PAD)
hp_ally.grid(row=7, column=2, padx=PAD, pady=PAD)
#Damage
lb_damage.grid(row=8, column=0, padx=PAD, pady=PAD)
dmg_enemy.grid(row=8, column=1, padx=PAD, pady=PAD)
dmg_ally.grid(row=8, column=2, padx=PAD, pady=PAD)
#Hit
lb_hit.grid(row=9, column=0, padx=PAD, pady=PAD)
hit_enemy.grid(row=9, column=1, padx=PAD, pady=PAD)
hit_ally.grid(row=9, column=2, padx=PAD, pady=PAD)
#Attack
lb_atk.grid(row=10, column=0, padx=PAD, pady=PAD)
atk_enemy.grid(row=10, column=1, padx=PAD, pady=PAD)
atk_ally.grid(row=10, column=2, padx=PAD, pady=PAD)
#Defense
lb_def.grid(row=11, column=0, padx=PAD, pady=PAD)
def_enemy.grid(row=11, column=1, padx=PAD, pady=PAD)
def_ally.grid(row=11, column=2, padx=PAD, pady=PAD)
#BATTLE PHASE
lb_battle_phase.grid(row=12, column=0, columnspan=3, sticky=tk.N, padx=PAD, pady=PAD)
#INITIAL
radio_initial.grid(row=13, column=0, padx=PAD, pady=PAD)
#Terrains
radio_terrain.grid(row=14, column=0, padx=PAD, pady=PAD)
om_enemy_terrain.grid(row=14, column=1)
om_ally_terrain.grid(row=14, column=2)
#Enemy Actions
radio_enemy_action.grid(row=15, column=0, padx=PAD, pady=PAD)
om_enemy_action.grid(row=15, column=1)
hp_dmg_enemy.grid(row=15, column=2)
ch_enemy_msg.grid(row=16, column=1)
#Ally Actions
radio_ally_action.grid(row=17, column=0, padx=PAD, pady=PAD)
om_ally_action.grid(row=17, column=1)
hp_dmg_ally.grid(row=17, column=2)
ch_ally_msg.grid(row=18, column=1)

# ----------------------- FRAME: RIGH SIDE ----------------------- #
fr_right_side = tk.Frame(root, borderwidth=2, relief='groove')
# ----------------------- FRAME: IMAGE PREVIEW ----------------------- #
fr_img_preview = tk.Frame(fr_right_side)
#IMAGE PREVIEW LABEL
lb_img_preview = tk.Label(fr_img_preview, text='Image Preview')
#ACTUAL IMAGE
back1 = Image.open(os.path.dirname(__file__)+r"\bg\bg1.png")
last_drawn = ImageTk.PhotoImage(back1)
back1.close()
lb_image = tk.Label(fr_img_preview, image=last_drawn)
#SCROLLBAR FOR TEXT LINES
fr_buttons = tk.Frame(fr_img_preview)
bt_up = tk.Button(fr_buttons, text='\u25B2', command=LineUp)
bt_down = tk.Button(fr_buttons, text='\u25BC', command=LineDown)
# ----------------------- GRIDDING IMAGE PREVIEW ----------------------- #
lb_img_preview.grid(row=0, column=0, columnspan=2, padx=PAD, pady=PAD)
lb_image.grid(row=1, column=0, rowspan=2, padx=PAD, pady=PAD)

bt_up.pack()
bt_down.pack()
fr_buttons.grid(row=2, column=1, sticky=tk.S, pady = 30)

fr_img_preview.grid(row=0, column=0)
# ----------------------- FRAME: FINAL MESSAGE ----------------------- #
final = tk.Frame(fr_right_side)
lb_options = tk.Label(final, text='Options for Final Message Box')
#Intial message
final_message = tk.StringVar()
om_final_message = ttk.OptionMenu(final, final_message, final_msg_options[0], *final_msg_options, command=DisableWidgets)
om_final_message.config(width=25, state='disabled')
#Gain EXP
gain_exp = tk.BooleanVar()
ch_gain_exp = tk.Checkbutton(final, text='Gain EXP', variable = gain_exp, state = 'disabled', command=DisableWidgets)
#Current EXP
lb_exp_current = tk.Label(final, text='Current EXP')
sp_exp_current = ttk.Spinbox(final, width=5, from_=0, to=100, command = DisableWidgets)
sp_exp_current.set(0)
sp_exp_current.config(state='disabled')
#Gained EXP
lb_exp_gained = tk.Label(final, text='Gained EXP')
sp_exp_gained = ttk.Spinbox(final, width=5, from_=1, to=99, command = DisableWidgets)
sp_exp_gained.set(1)
sp_exp_gained.config(state='disabled')
#Drop Item
drop_item = tk.BooleanVar()
ch_drop_item = tk.Checkbutton(final, text='Item Drop', variable = drop_item, state = 'disabled', command=DisableWidgets)

dropped = tk.StringVar(value="Iron Sword")
menubutton = ttk.Menubutton(final, textvariable=dropped, width=10)
main_menu = tk.Menu(menubutton, tearoff=False)
menubutton.configure(menu=main_menu)
for item in (["Swords"] + swords,
             ["Lances"] + lances,
             ["Axes"] + axes,
             ["Bows"] + bows,
             ["Ballistae"] + ballistae,
             ["Dragonstones"] + dragonstones,
             ["Tomes"] + tomes,
             ["Staves"] + staves,
             ["Items"] + items):
    menu = tk.Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label=item[0], menu=menu)
    for value in item[1:]:
        menu.add_radiobutton(value=value, label=value, variable=dropped, command=UpdateImg)
menubutton.config(state='disabled')

#Level Up stats
lv_up = tk.BooleanVar()
ch_lv_up = tk.Checkbutton(final, text='Show Level up text', variable = lv_up,
                          state = 'disabled', command=DisableWidgets)
#strength, skill, luck, weapon lv, speed, max hp
lv_str = tk.BooleanVar()
ch_lv_str = tk.Checkbutton(final, text='Strength +1', variable = lv_str,
                          state = 'disabled', command=DisableWidgets)
lv_skl = tk.BooleanVar()
ch_lv_skl = tk.Checkbutton(final, text='Skill +1', variable = lv_skl,
                          state = 'disabled', command=DisableWidgets)
lv_lck = tk.BooleanVar()
ch_lv_lck = tk.Checkbutton(final, text='Luck +1', variable = lv_lck,
                          state = 'disabled', command=DisableWidgets)
lv_wpn = tk.BooleanVar()
ch_lv_wpn = tk.Checkbutton(final, text='Weapon Lv. +1', variable = lv_wpn,
                          state = 'disabled', command=DisableWidgets)
lv_spd = tk.BooleanVar()
ch_lv_spd = tk.Checkbutton(final, text='Speed +1', variable = lv_spd,
                          state = 'disabled', command=DisableWidgets)
lv_hp = tk.BooleanVar()
ch_lv_hp = tk.Checkbutton(final, text='Max HP +1', variable = lv_hp,
                          state = 'disabled', command=DisableWidgets)
#EXP BOX
exp_box = tk.BooleanVar()
ch_exp_box = tk.Checkbutton(final, text='EXP Box', variable=exp_box,
                            state='disabled', command=DisableWidgets)
#SAVE BUTTON
bt_save = tk.Button(final, text='Save Image', command=SaveImage)

# ----------------------- GRIDDING THE WIDGETS ----------------------- #
lb_options.grid(row=0, column=0, columnspan=5, sticky=tk.N, padx = PAD, pady = PAD)

om_final_message.grid(row=1, column=0, columnspan=3, sticky=tk.W, padx = PAD, pady = PAD)
ch_gain_exp.grid(row=1, column=3, sticky=tk.W)

lb_exp_current.grid(row=2, column=0, sticky=tk.W, padx = PAD, pady = PAD)
sp_exp_current.grid(row=2, column=1, sticky=tk.W, padx = PAD, pady = PAD)
lb_exp_gained.grid(row=2, column=2, sticky=tk.W, padx = PAD, pady = PAD)
sp_exp_gained.grid(row=2, column=3, sticky=tk.W, padx = PAD, pady = PAD)

ch_drop_item.grid(row=3, column=0, sticky=tk.W, padx = PAD, pady = PAD)
menubutton.grid(row=3, column=2, sticky=tk.W, padx = PAD, pady = PAD)

ch_lv_up.grid(row=4, column=0, columnspan=2, sticky=tk.W, padx = PAD, pady = PAD)
ch_lv_str.grid(row=5, column=0, columnspan=2, sticky=tk.W, padx = PAD+10, pady = PAD)
ch_lv_skl.grid(row=6, column=0, columnspan=2, sticky=tk.W, padx = PAD+10, pady = PAD)
ch_lv_lck.grid(row=7, column=0, columnspan=2, sticky=tk.W, padx = PAD+10, pady = PAD)
ch_lv_wpn.grid(row=5, column=2, columnspan=2, sticky=tk.W, padx = PAD, pady = PAD)
ch_lv_spd.grid(row=6, column=2, columnspan=2, sticky=tk.W, padx = PAD, pady = PAD)
ch_lv_hp.grid(row=7, column=2, columnspan=2, sticky=tk.W, padx = PAD, pady = PAD)

ch_exp_box.grid(row=8, column=0, sticky=tk.W, padx = PAD, pady = PAD)
bt_save.grid(row=9, column=0, columnspan=4, sticky=tk.N, padx = PAD, pady = PAD + 4)
# ----------------------- GRIDDING THE FRAMES ----------------------- #
fr_left_side.grid(row=0, column=0, padx=20)
fr_right_side.grid(row=0, column=1, sticky=tk.N)
final.grid(row=1, column=0)

# ----------------------- FIRST UPDATE + MAINLOOP ----------------------- #
line = 1
will_save = False
UpdateImg()
root.mainloop()