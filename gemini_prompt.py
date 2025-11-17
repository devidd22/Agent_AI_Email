from google import genai
from dotenv import load_dotenv
from datetime import datetime
def aplicare_gemini():
    load_dotenv()
    client = genai.Client()

    with open("plain_text.txt", "r") as f:
        data = f.read().split()
    data = '\n'.join(data)
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=f"""
You are a professional newsletter writer and email designer. Given article text separated by "New Article" markers, create a polished HTML newsletter in the style of premium tech newsletters (TL;DR AI, Morning Brew, The Hustle).

INPUT FORMAT:
Articles are separated by the line "New Article". Group related articles (covering the same topic/event) and create unified summaries for each group.

INSTRUCTIONS:

1. NEWSLETTER STRUCTURE
- Title: "TL;DR DAIVID — {datetime.today().strftime('%Y-%m-%d')}"
- TL;DR Section (top of newsletter):
  * Eye-catching colored background (#667eea to #764ba2 gradient or similar)
  * 3 bullet points maximum
  * Each bullet with relevant emoji
  * Highlight the most important insights across all articles

2. MAIN CONTENT SECTIONS

📰 Headlines & Launches (2–4 items)
- Group related articles about the same topic/launch
- Create a unified summary for each group
- Bold the main subject/company name
- 1-2 sentences per item

🔎 Deep Dives & Analysis (3–5 items)
- Detailed summaries of grouped articles
- Include key insights, numbers, implications
- 2-3 sentences per item
- Use bold for important terms

📌 Quick Takes (3–5 items)
- Actionable insights or notable mentions
- "What this means:" style explanations
- Short, punchy bullets

🔗 Sources & Further Reading
- Styled button/link to original sources
- Clean, professional appearance

3. DESIGN REQUIREMENTS

Visual Style:
- Modern, clean design with professional color scheme
- Gradient backgrounds for key sections
- Rounded corners (8-12px) on containers
- Generous padding and spacing
- Subtle shadows for depth

Typography:
- Use system fonts: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif
- Clear hierarchy: titles (24-28px), section headers (20-22px), body (16px)
- Line height: 1.6 for readability
- Bold for emphasis, not excessive

Colors & Styling:
- Primary accent: Modern blues/purples (#667eea, #764ba2, #4F46E5)
- Background: Light gray (#F9FAFB) or white (#FFFFFF)
- Text: Dark gray (#1F2937) for body, black (#111827) for headers
- Links: Vibrant blue (#2563EB) with hover states
- Borders: Subtle (#E5E7EB)

Layout:
- Max width: 600px (Gmail-safe)
- All CSS inline (Gmail compatibility)
- Responsive padding: 20-30px
- Section spacing: 24-32px between sections
- Card-style containers with background colors

Interactive Elements:
- Styled buttons with gradients or solid colors
- Hover effects via inline styles where possible
- Clear call-to-action styling

4. CONTENT PROCESSING

Article Grouping:
- Identify articles covering the same story/topic
- Merge their content into single, cohesive summaries
- Avoid repetition across sections
- Prioritize unique insights from each source

Summary Writing:
- Start with the most newsworthy element
- Include specific numbers, dates, names
- Explain "why it matters"
- Keep language clear and jargon-free
- Use active voice

5. OUTPUT FORMAT
- HTML only — no markdown code fences, no commentary
- Fully self-contained with inline CSS
- Ready to copy/paste directly into Gmail
- Tested for Gmail compatibility (no external stylesheets, JavaScript, or unsupported CSS)

6. QUALITY REQUIREMENTS
- All related articles must be summarized together
- No duplicate information across sections
- Visual hierarchy is clear
- Emojis used purposefully (not excessively)
- Colors are professional and readable
- All text is concise and scannable
- Links and buttons are properly styled
- Layout works in Gmail web and mobile

INPUT ARTICLES:
---BEGIN---
{data}
---END---

Generate the complete HTML newsletter now. Output HTML only, no explanations.
"""
    )

    with open("afisare_prompt.html", "w") as f:
        f.write(response.text)
    print("Fisierul HTML a fost scris cu succes!")