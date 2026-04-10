import pygame
import sys

# Başlatma
pygame.init()

# Ekran boyutu (Android uyumlu - 9:16 oranı)
SCREEN_W = 480
SCREEN_H = 854

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Bilgi Yarışması")

clock = pygame.time.Clock()

# ─── RENKLER ───────────────────────────────────────────────────────────────
BG_COLOR       = (15, 20, 40)
CARD_COLOR     = (25, 35, 65)
CARD_BORDER    = (60, 100, 200)
BTN_START      = (50, 180, 120)
BTN_START_H    = (70, 210, 150)
BTN_SHOW       = (60, 120, 220)
BTN_SHOW_H     = (90, 150, 255)
BTN_NEXT       = (180, 80, 220)
BTN_NEXT_H     = (210, 110, 255)
BTN_RESTART    = (220, 130, 40)
BTN_RESTART_H  = (255, 160, 70)
TEXT_WHITE     = (240, 245, 255)
TEXT_LIGHT     = (180, 200, 240)
TEXT_GOLD      = (255, 210, 80)
TEXT_GREEN     = (80, 220, 140)
SHADOW         = (5, 10, 25)
ACCENT         = (100, 160, 255)
STAR_COLOR     = (255, 220, 80)

# ─── YARDIMCI: Türkçe karakter desteği için font ───────────────────────────
def get_font(size, bold=False):
    # Android'de font dosyası bulamazsa hata vermemesi için SysFont'a düşür
    try:
        return pygame.font.SysFont("sans-serif", size, bold=bold)
    except:
        return pygame.font.Font(None, size)
# ─── FONTLAR ───────────────────────────────────────────────────────────────
font_title   = get_font(42, bold=True)
font_sub     = get_font(22)
font_btn     = get_font(26, bold=True)
font_q       = get_font(24, bold=True)
font_a       = get_font(22)
font_counter = get_font(20)
font_small   = get_font(18)
font_finish  = get_font(36, bold=True)

# ─── SORU ve CEVAPLAR ──────────────────────────────────────────────────────
QA = [
    ("Dünyanın en uzun nehri olan Nil'in uzunluğu kaç kilometredir?", "6.650 km"),
    ("Bir filin kalbi kaç kilogram ağırlığındadır?", "Yaklaşık 12-21 kg"),
    ("Dünyanın en yüksek dağı Everest'in zirve yüksekliği kaç metredir?", "8.849 metre"),
    ("Bir zürafanın boynu kaç omurdan oluşur?", "7 omur (insanla aynı)"),
    ("Işığın boşluktaki hızı saniyede kaç kilometredir?", "299.792 km/s"),
    ("Dünya'nın çevresi yaklaşık kaç kilometredir?", "40.075 km"),
    ("Bir insan vücudunda yaklaşık kaç litre kan dolaşır?", "4,5 ile 5,5 litre"),
    ("Amazon Nehri'nin uzunluğu kaç kilometredir?", "6.400 km"),
    ("Bir balinanın kalbi kaç kilogram ağırlığındadır?", "Yaklaşık 180-200 kg"),
    ("Dünyanın en derin gölü Baykal Gölü'nün derinliği kaç metredir?", "1.642 metre"),
    ("İnsan vücudunda kaç kemik bulunur?", "206 kemik"),
    ("Bir ahtapotun kalp sayısı kaçtır?", "3 kalp"),
    ("Saatte 100 km hızla giden bir araç 1 dakikada kaç metre yol alır?", "1.666 metre"),
    ("Dünyanın en büyük okyanusu Pasifik'in yüzey alanı kaç km²'dir?", "165,2 milyon km²"),
    ("Bir deve hörgücünde yaklaşık kaç kilogram yağ depolanır?", "Yaklaşık 36 kg"),
    ("Türkiye'nin en yüksek dağı Ağrı'nın yüksekliği kaç metredir?", "5.137 metre"),
    ("İnsan beyni yaklaşık kaç milyar nöron içerir?", "86 milyar nöron"),
    ("Bir karıncanın kendi ağırlığının kaç katını taşıyabilir?", "Ağırlığının 50 katını"),
    ("Dünyanın en büyük çölü Antarktika'nın yüzey alanı kaç km²'dir?", "14,2 milyon km²"),
    ("Bir zürafanın dili kaç santimetre uzunluğundadır?", "45-50 cm"),
    ("Güneş'in çapı Dünya'nın çapının kaç katıdır?", "109 katı"),
    ("Bir insan kalbi günde yaklaşık kaç kez atar?", "100.000 kez"),
    ("Dünyanın en büyük adası Grönland'ın yüzey alanı kaç km²'dir?", "2,1 milyon km²"),
    ("Bir fil günde kaç kilogram yiyecek tüketir?", "136-270 kg"),
    ("Mariana Çukuru'nun en derin noktası kaç metredir?", "11.034 metre"),
    ("Bir insan ortalama kaç yıl yaşar? (dünya ortalaması)", "72-73 yıl"),
    ("Asya'nın yüzey alanı kaç km²'dir?", "44,6 milyon km²"),
    ("Bir çita maksimum kaç km/s hıza ulaşabilir?", "120 km/s"),
    ("Güneş'in Dünya'ya olan ortalama uzaklığı kaç km'dir?", "149,6 milyon km"),
    ("Bir penguen su altında dakikada kaç kez yüzgeç çırpar?", "Dakikada 80-100 kez"),
    ("İnsanın derisi vücudun toplam ağırlığının yüzde kaçını oluşturur?", "Yaklaşık yüzde 16"),
    ("Bir ahtapotun kaç kolu vardır?", "8 kol"),
    ("Dünyanın en uzun duvarı Çin Seddi kaç kilometre uzunluğundadır?", "21.196 km"),
    ("Bir timsah dişini ömrü boyunca kaç kez yeniler?", "45-50 kez"),
    ("Ekvador'daki Chimborazo Dağı, Dünya'nın merkezinden kaç km uzaktadır?", "6.384 km"),
    ("Bir insan günde ortalama kaç kez göz kırpar?", "15.000-20.000 kez"),
    ("Satürn'ün halkalarının genişliği kaç km'dir?", "282.000 km"),
    ("Bir arının kovana bir kez bal taşımasıyla kaç gram bal üretebilir?", "Ömrü boyunca 1/12 çay kaşığı"),
    ("Dünyanın en uzun demiryolu olan Trans-Sibirya'nın uzunluğu kaç km'dir?", "9.289 km"),
    ("Bir denizanasının vücudunun yüzde kaçı sudur?", "Yüzde 95"),
    ("Ay'ın Dünya'ya olan ortalama uzaklığı kaç km'dir?", "384.400 km"),
    ("Bir tiranozor reks'in dişi kaç santimetre uzunluğundadır?", "30 cm"),
    ("İnsan vücudundaki toplam damar uzunluğu kaç km'dir?", "96.000 km"),
    ("Bir kartalın kanat açıklığı maksimum kaç santimetredir?", "240 cm (Kel Kartal)"),
    ("Dünyanın en büyük volkanı Mauna Loa'nın yüksekliği kaç metredir?", "4.169 metre (denizden)"),
    ("Bir aslanın çığlığı kaç km uzaktan duyulabilir?", "8 km"),
    ("Uzay boşluğunun sıcaklığı yaklaşık kaç derecedir?", "-270,45 °C"),
    ("Bir insan ömrü boyunca ortalama kaç km yürür?", "160.000 km"),
    ("Dünyanın en büyük canlısı mavi balinanın boyu kaç metredir?", "30 metre"),
    ("Bir köpeğin burnu insandan kaç kat daha hassastır?", "10.000 ila 100.000 kat"),
]

# ─── YARDIMCI FONKSİYONLAR ────────────────────────────────────────────────
def draw_rounded_rect(surf, color, rect, radius=18, border_color=None, border_width=0):
    pygame.draw.rect(surf, color, rect, border_radius=radius)
    if border_color and border_width > 0:
        pygame.draw.rect(surf, border_color, rect, border_width, border_radius=radius)

def draw_shadow(surf, rect, radius=18, alpha=80):
    shadow_surf = pygame.Surface((rect[2] + 8, rect[3] + 8), pygame.SRCALPHA)
    pygame.draw.rect(shadow_surf, (*SHADOW, alpha), (4, 4, rect[2], rect[3]), border_radius=radius)
    surf.blit(shadow_surf, (rect[0] - 2, rect[1] + 2))

def wrap_text(text, font, max_width):
    """Metni verilen genişliğe göre satırlara böler."""
    words = text.split(" ")
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if font.size(test)[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def render_wrapped_text(surf, text, font, color, rect, line_spacing=8):
    """Metni rect içine ortalayarak çizer, toplam yüksekliği döndürür."""
    lines = wrap_text(text, font, rect[2])
    total_h = len(lines) * (font.get_height() + line_spacing)
    y = rect[1] + (rect[3] - total_h) // 2
    for line in lines:
        rendered = font.render(line, True, color)
        x = rect[0] + (rect[2] - rendered.get_width()) // 2
        surf.blit(rendered, (x, y))
        y += font.get_height() + line_spacing
    return total_h

def draw_button(surf, text, rect, color, hover_color, mouse_pos, font, text_color=TEXT_WHITE, radius=16):
    is_hover = pygame.Rect(rect).collidepoint(mouse_pos)
    c = hover_color if is_hover else color
    draw_shadow(surf, rect, radius)
    draw_rounded_rect(surf, c, rect, radius)
    txt = font.render(text, True, text_color)
    surf.blit(txt, (rect[0] + (rect[2] - txt.get_width()) // 2,
                    rect[1] + (rect[3] - txt.get_height()) // 2))
    return is_hover

def draw_stars(surf, count=20):
    """Arka plana dekoratif yıldızlar çizer (sabit seed ile)."""
    import random
    rng = random.Random(42)
    for _ in range(count):
        x = rng.randint(0, SCREEN_W)
        y = rng.randint(0, SCREEN_H)
        r = rng.randint(1, 3)
        alpha = rng.randint(60, 180)
        s = pygame.Surface((r*2, r*2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*STAR_COLOR, alpha), (r, r), r)
        surf.blit(s, (x, y))

def draw_progress_bar(surf, current, total, x, y, w, h):
    bg_rect = (x, y, w, h)
    draw_rounded_rect(surf, (40, 50, 80), bg_rect, 8)
    if total > 0:
        fill_w = int(w * (current / total))
        if fill_w > 0:
            fill_rect = (x, y, fill_w, h)
            draw_rounded_rect(surf, ACCENT, fill_rect, 8)
    border_s = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(border_s, (*ACCENT, 100), (0, 0, w, h), 2, border_radius=8)
    surf.blit(border_s, (x, y))

# ─── EKRANLAR ──────────────────────────────────────────────────────────────
def draw_home(surf, mouse_pos):
    surf.fill(BG_COLOR)
    draw_stars(surf)

    # Başlık kartı
    card_x, card_y, card_w, card_h = 40, 120, SCREEN_W - 80, 280
    draw_shadow(surf, (card_x, card_y, card_w, card_h), 24)
    draw_rounded_rect(surf, CARD_COLOR, (card_x, card_y, card_w, card_h), 24, CARD_BORDER, 2)

    title = font_title.render("🧠 Bilgi", True, TEXT_GOLD)
    title2 = font_title.render("Yarışması", True, TEXT_WHITE)
    surf.blit(title,  (card_x + (card_w - title.get_width()) // 2,  card_y + 40))
    surf.blit(title2, (card_x + (card_w - title2.get_width()) // 2, card_y + 95))

    sub = font_sub.render(f"{len(QA)} Soru · Kendini Test Et!", True, TEXT_LIGHT)
    surf.blit(sub, (card_x + (card_w - sub.get_width()) // 2, card_y + 175))

    # İkon çizimi
    icon = font_title.render("⭐", True, STAR_COLOR)
    surf.blit(icon, (card_x + (card_w - icon.get_width()) // 2, card_y + 220))

    # Başla butonu
    btn_rect = (SCREEN_W // 2 - 130, 460, 260, 65)
    draw_button(surf, "▶  OYUNA BAŞLA", btn_rect,
                BTN_START, BTN_START_H, mouse_pos, font_btn)

    # Alt bilgi
    hint = font_small.render("Soruyu oku · Cevabı tahmin et · İlerle", True, TEXT_LIGHT)
    surf.blit(hint, ((SCREEN_W - hint.get_width()) // 2, 560))

    return btn_rect


def draw_question(surf, mouse_pos, index, show_answer):
    surf.fill(BG_COLOR)
    draw_stars(surf, 10)

    q_text, a_text = QA[index]

    # Üst bar: sayaç + ilerleme
    counter = font_counter.render(f"Soru {index + 1} / {len(QA)}", True, ACCENT)
    surf.blit(counter, (30, 30))
    draw_progress_bar(surf, index + 1, len(QA), 30, 60, SCREEN_W - 60, 10)

    # Soru kartı
    q_card = (20, 100, SCREEN_W - 40, 240)
    draw_shadow(surf, q_card, 20)
    draw_rounded_rect(surf, CARD_COLOR, q_card, 20, CARD_BORDER, 2)

    label = font_small.render("SORU", True, ACCENT)
    surf.blit(label, (q_card[0] + 20, q_card[1] + 18))

    text_rect = (q_card[0] + 20, q_card[1] + 50, q_card[2] - 40, q_card[3] - 60)
    render_wrapped_text(surf, q_text, font_q, TEXT_WHITE, text_rect, line_spacing=10)

    if not show_answer:
        # Cevabı Göster butonu
        btn_rect = (SCREEN_W // 2 - 140, 380, 280, 62)
        draw_button(surf, "👁  CEVABI GÖSTER", btn_rect,
                    BTN_SHOW, BTN_SHOW_H, mouse_pos, font_btn)
        return btn_rect, None

    else:
        # Cevap kartı
        a_card = (20, 370, SCREEN_W - 40, 200)
        draw_shadow(surf, a_card, 20)
        draw_rounded_rect(surf, (20, 45, 35), a_card, 20, BTN_SHOW, 2)

        a_label = font_small.render("CEVAP", True, TEXT_GREEN)
        surf.blit(a_label, (a_card[0] + 20, a_card[1] + 14))

        a_text_rect = (a_card[0] + 20, a_card[1] + 45, a_card[2] - 40, a_card[3] - 55)
        render_wrapped_text(surf, a_text, font_a, TEXT_GREEN, a_text_rect, line_spacing=8)

        # Sonraki soru / Bitir butonu
        is_last = (index == len(QA) - 1)
        label_next = "🏁  BİTİR" if is_last else "➡  SONRAKİ SORU"
        btn_next = (SCREEN_W // 2 - 140, 610, 280, 62)
        draw_button(surf, label_next, btn_next,
                    BTN_NEXT, BTN_NEXT_H, mouse_pos, font_btn)
        return None, btn_next


def draw_finish(surf, mouse_pos):
    surf.fill(BG_COLOR)
    draw_stars(surf)

    # Tebrik kartı
    card = (30, 150, SCREEN_W - 60, 340)
    draw_shadow(surf, card, 24)
    draw_rounded_rect(surf, CARD_COLOR, card, 24, TEXT_GOLD, 2)

    trophy = font_finish.render("🏆", True, TEXT_GOLD)
    surf.blit(trophy, (card[0] + (card[2] - trophy.get_width()) // 2, card[1] + 30))

    tebrik = font_finish.render("Tebrikler!", True, TEXT_GOLD)
    surf.blit(tebrik, (card[0] + (card[2] - tebrik.get_width()) // 2, card[1] + 105))

    msg1 = font_sub.render("Tüm soruları tamamladın.", True, TEXT_WHITE)
    msg2 = font_sub.render(f"{len(QA)} soruyu başarıyla geçtin! 🎉", True, TEXT_LIGHT)
    surf.blit(msg1, (card[0] + (card[2] - msg1.get_width()) // 2, card[1] + 185))
    surf.blit(msg2, (card[0] + (card[2] - msg2.get_width()) // 2, card[1] + 225))

    stars_row = font_finish.render("⭐ ⭐ ⭐", True, STAR_COLOR)
    surf.blit(stars_row, (card[0] + (card[2] - stars_row.get_width()) // 2, card[1] + 275))

    # Tekrar Oyna butonu
    btn_rect = (SCREEN_W // 2 - 130, 540, 260, 65)
    draw_button(surf, "🔄  TEKRAR OYNA", btn_rect,
                BTN_RESTART, BTN_RESTART_H, mouse_pos, font_btn)

    return btn_rect


# ─── ANA DÖNGÜ ─────────────────────────────────────────────────────────────
def main():
    # EKRAN: "home" | "question" | "finish"
    screen_state  = "home"
    question_idx  = 0
    show_answer   = False

    while True:
        mouse_pos = pygame.mouse.get_pos()
        click     = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.FINGERDOWN):
                click = True

        # ── HOME ──────────────────────────────────────────────────────────
        if screen_state == "home":
            btn_start = draw_home(screen, mouse_pos)
            if click and pygame.Rect(btn_start).collidepoint(mouse_pos):
                question_idx = 0
                show_answer  = False
                screen_state = "question"

        # ── QUESTION ──────────────────────────────────────────────────────
        elif screen_state == "question":
            btn_show, btn_next = draw_question(screen, mouse_pos,
                                               question_idx, show_answer)
            if click:
                if btn_show and pygame.Rect(btn_show).collidepoint(mouse_pos):
                    show_answer = True
                if btn_next and pygame.Rect(btn_next).collidepoint(mouse_pos):
                    if question_idx < len(QA) - 1:
                        question_idx += 1
                        show_answer   = False
                    else:
                        screen_state = "finish"

        # ── FINISH ────────────────────────────────────────────────────────
        elif screen_state == "finish":
            btn_restart = draw_finish(screen, mouse_pos)
            if click and pygame.Rect(btn_restart).collidepoint(mouse_pos):
                question_idx = 0
                show_answer  = False
                screen_state = "home"

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
