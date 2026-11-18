"""Build the branded printable recipe PDF from the supplied Markdown source."""

from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, HRFlowable, Image, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer,
)
from PIL import Image as PILImage, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "kovaszos_receptek.md"
DEST = ROOT / "letoltheto" / "hajnal-kovaszos-receptek.pdf"
DEST.parent.mkdir(exist_ok=True)

pdfmetrics.registerFont(TTFont("Georgia", r"C:\Windows\Fonts\georgia.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Bold", r"C:\Windows\Fonts\georgiab.ttf"))
pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold")

INK = colors.HexColor("#2F241D")
CRUST = colors.HexColor("#874622")
CHERRY = colors.HexColor("#9B3E3A")
OAT = colors.HexColor("#D9C8B1")
CREAM = colors.HexColor("#FFF9EE")
PAPER = colors.HexColor("#F3E8D2")

styles = {
    "title": ParagraphStyle("Title", fontName="Georgia-Bold", fontSize=29, leading=34, textColor=INK, spaceAfter=10),
    "poster-title": ParagraphStyle("PosterTitle", fontName="Georgia-Bold", fontSize=40, leading=41, textColor=INK, spaceAfter=14, alignment=TA_CENTER),
    "poster-line": ParagraphStyle("PosterLine", fontName="Georgia-Bold", fontSize=17, leading=22, textColor=INK, spaceAfter=18, alignment=TA_CENTER),
    "subtitle": ParagraphStyle("Subtitle", fontName="Arial", fontSize=11, leading=16, textColor=INK, spaceAfter=14),
    "h1": ParagraphStyle("Recipe", fontName="Georgia-Bold", fontSize=21, leading=25, textColor=INK, spaceBefore=5, spaceAfter=10, keepWithNext=True),
    "h2": ParagraphStyle("Section", fontName="Arial-Bold", fontSize=10.5, leading=14, textColor=CRUST, spaceBefore=12, spaceAfter=6, keepWithNext=True),
    "body": ParagraphStyle("Body", fontName="Arial", fontSize=11, leading=16.5, textColor=INK, spaceAfter=7),
    "bullet": ParagraphStyle("Bullet", fontName="Arial", fontSize=11, leading=16.5, textColor=INK, leftIndent=14, firstLineIndent=-10, spaceAfter=3),
    "step": ParagraphStyle("Step", fontName="Arial", fontSize=11, leading=16.5, textColor=INK, leftIndent=19, firstLineIndent=-17, spaceAfter=7),
    "eyebrow": ParagraphStyle("Eyebrow", fontName="Arial-Bold", fontSize=8.5, leading=11, textColor=CHERRY, spaceAfter=8),
}

def rich(s):
    s = html.escape(s)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)

class CoverPoster(Flowable):
    def __init__(self):
        super().__init__()
        self.width = 495
        self.height = 156

    def draw(self):
        c = self.canv
        c.setFillColor(CREAM)
        c.setStrokeColor(CHERRY)
        c.setLineWidth(1.4)
        c.rect(2, 2, self.width - 4, self.height - 4, fill=1, stroke=1)
        c.rect(8, 8, self.width - 16, self.height - 16, fill=0, stroke=1)
        c.setFillColor(CHERRY)
        c.setFont("Arial-Bold", 9)
        c.drawCentredString(self.width / 2, 128, "A KIS PÉKSÉG A SARKON  ·  PÉCS")
        c.setFillColor(INK)
        c.setFont("Georgia-Bold", 29)
        c.drawCentredString(self.width / 2, 98, "HAJNAL")
        c.drawCentredString(self.width / 2, 62, "KOVÁSZOS")
        c.drawCentredString(self.width / 2, 26, "RECEPTEK")

class RecipeLabel(Flowable):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.width = 155
        self.height = 25

    def draw(self):
        c = self.canv
        c.setStrokeColor(CHERRY)
        c.setLineWidth(1)
        c.rect(0, 3, 151, 20, fill=0, stroke=1)
        c.setFillColor(CHERRY)
        c.setFont("Arial-Bold", 8.5)
        c.drawString(10, 10, f"HAJNAL RECEPT 0{self.number}")

class RecipeDoc(BaseDocTemplate):
    def __init__(self, path):
        super().__init__(str(path), pagesize=A4, leftMargin=50, rightMargin=50,
                         topMargin=93, bottomMargin=54, title="Hajnal kovászos receptek")
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates(PageTemplate(id="recipe", frames=frame, onPage=self.decorate))

    def decorate(self, canvas, doc):
        w, h = A4
        canvas.saveState()
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, w, h, stroke=0, fill=1)
        canvas.setFillColor(INK)
        canvas.rect(0, h - 21, w, 21, stroke=0, fill=1)
        canvas.setFont("Arial-Bold", 7)
        canvas.setFillColor(CREAM)
        canvas.drawString(50, h - 14, "PÉCS BELVÁROSÁBAN")
        canvas.drawRightString(w - 50, h - 14, "KOVÁSZOS PÉKSÉG")
        canvas.setStrokeColor(CHERRY)
        canvas.setLineWidth(2)
        canvas.arc(50, h - 65, 76, h - 39, 0, 180)
        canvas.line(49, h - 65, 77, h - 65)
        canvas.line(63, h - 34, 63, h - 29)
        canvas.line(46, h - 35, 50, h - 39)
        canvas.line(80, h - 35, 76, h - 39)
        canvas.setFont("Georgia-Bold", 20)
        canvas.setFillColor(INK)
        canvas.drawString(85, h - 58, "HAJNAL")
        canvas.setStrokeColor(INK)
        canvas.setLineWidth(1.1)
        canvas.line(50, h - 80, w - 50, h - 80)
        canvas.setFillColor(INK)
        canvas.rect(0, 0, w, 35, stroke=0, fill=1)
        canvas.setFont("Arial", 8)
        canvas.setFillColor(CREAM)
        canvas.drawString(50, 14, "HAJNAL  ·  KOVÁSZOS PÉKSÉG  ·  PÉCS")
        canvas.drawRightString(w - 50, 14, f"{doc.page}.")
        canvas.restoreState()

lines = SOURCE.read_text(encoding="utf-8").splitlines()
story = []
intro = lines[2].strip()
story += [Spacer(1, 7), CoverPoster(), Spacer(1, 17),
          Paragraph("A jó reggel, a jó kenyérnél kezdődik.", styles["poster-line"]),
          Paragraph(intro, styles["subtitle"])]

photo = ROOT / "képek" / "pexels-aygnedalya-296473942-24245229.jpg"
crop_path = ROOT / "tervezes" / "pdf-ellenorzes" / "borito-kep.jpg"
crop_path.parent.mkdir(exist_ok=True)
with PILImage.open(photo) as original:
    cropped = ImageOps.fit(original.convert("RGB"), (1500, 560), method=PILImage.Resampling.LANCZOS, centering=(0.5, 0.47))
    cropped.save(crop_path, quality=86)
photo_width = 495
photo_height = 185
story.append(Image(str(crop_path), width=photo_width, height=photo_height, kind="direct"))
story.append(Spacer(1, 15))
story.append(Paragraph("Három recept egy nyugodtabb reggelhez", styles["h2"]))
story.append(Paragraph("Klasszikus fehér kenyér · magvas teljes kiőrlésű kenyér · kovászos zsemle", styles["body"]))
story.append(Spacer(1, 8))

in_intro = True
for line in lines[3:]:
    s = line.strip()
    if not s or s == "---":
        continue
    if s.startswith("## "):
        in_intro = False
        story.append(PageBreak())
        title = s[3:]
        story.append(RecipeLabel(len([x for x in story if isinstance(x, RecipeLabel)]) + 1))
        story.append(Paragraph(rich(title), styles["h1"]))
        story.append(HRFlowable(width="100%", thickness=1, color=CHERRY, spaceAfter=11))
    elif s.startswith("**") and s.endswith("**") and s.count("**") == 2:
        story.append(Paragraph(rich(s), styles["h2"]))
    elif s.startswith("- "):
        story.append(Paragraph("• " + rich(s[2:]), styles["bullet"]))
    elif re.match(r"^\d+\. ", s):
        num, content = s.split(". ", 1)
        story.append(Paragraph(f"<font color='#9B3E3A'><b>{num}.</b></font>  {rich(content)}", styles["step"]))
    elif s.startswith("**Tipp:**"):
        story.append(Spacer(1, 5))
        story.append(Paragraph(rich(s), styles["body"]))
    else:
        story.append(Paragraph(rich(s), styles["body"]))

doc = RecipeDoc(DEST)
doc.build(story)
print(DEST)
